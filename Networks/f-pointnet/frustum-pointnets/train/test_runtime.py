''' Evaluating Frustum PointNets.
Write evaluation results to KITTI format labels.
and [optionally] write results to pickle files.

Author: Charles R. Qi
Date: September 2017
'''
from __future__ import print_function

from tensorflow.python.client import timeline 
import os
import sys
import argparse
import importlib
import numpy as np
import tensorflow as tf
import cPickle as pickle
from timeit import default_timer as timer 
from tensorflow.python.profiler import model_analyzer
from tensorflow.python.profiler import option_builder 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'models'))
from model_util import NUM_HEADING_BIN, NUM_SIZE_CLUSTER
import provider
from parser import *
import statistics
from train_util import get_batch

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', type=int, default=0, help='GPU to use [default: GPU 0]')
parser.add_argument('--num_point', type=int, default=1024, help='Point Number [default: 1024]')
parser.add_argument('--model', default='frustum_pointnets_v2', help='Model name [default: frustum_pointnets_v1]')
parser.add_argument('--model_path', default='log_v2/model.ckpt', help='model checkpoint file path [default: log/model.ckpt]')
parser.add_argument('--batch_size', type=int, default=1, help='batch size for inference [default: 32]')
parser.add_argument('--output', default='test_results', help='output file/folder name [default: test_results]')
parser.add_argument('--data_path', default=None, help='frustum dataset pickle filepath [default: None]')
parser.add_argument('--from_rgb_detection', default=True, action='store_true', help='test from dataset files from rgb detection.')
parser.add_argument('--idx_path', default=None, help='filename of txt where each line is a data idx, used for rgb detection -- write <id>.txt for all frames. [default: None]')
parser.add_argument('--dump_result', action='store_true', help='If true, also dump results to .pickle file')
FLAGS = parser.parse_args()

# Set training configurations
BATCH_SIZE = FLAGS.batch_size
MODEL_PATH = FLAGS.model_path
NUM_POINT = FLAGS.num_point
GPU_INDEX = FLAGS.gpu
MODEL = importlib.import_module(FLAGS.model)
NUM_CLASSES = 2
NUM_CHANNEL = 4
total_time = 0.0
RUN_SIZE = 500

# Load Frustum Datasets.
TEST_DATASET = provider.FrustumDataset(npoints=NUM_POINT, split='val',
    rotate_to_center=True, overwritten_data_path=FLAGS.data_path,
    from_rgb_detection=FLAGS.from_rgb_detection, one_hot=True)

def get_session_and_ops(batch_size, num_point):
    ''' Define model graph, load model parameters,
    create session and return session handle and tensors
    '''
    with tf.Graph().as_default():
        with tf.device('/gpu:'+str(GPU_INDEX)):
            pointclouds_pl, one_hot_vec_pl, labels_pl, centers_pl, \
            heading_class_label_pl, heading_residual_label_pl, \
            size_class_label_pl, size_residual_label_pl = \
                MODEL.placeholder_inputs(batch_size, num_point)
            is_training_pl = tf.placeholder(tf.bool, shape=())
            
            print("pointclouds_pl: ", pointclouds_pl.shape)
            end_points = MODEL.get_model(pointclouds_pl, one_hot_vec_pl,
                is_training_pl)
            loss = MODEL.get_loss(labels_pl, centers_pl,
                heading_class_label_pl, heading_residual_label_pl,
                size_class_label_pl, size_residual_label_pl, end_points)
            saver = tf.train.Saver()

        # Create a session
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        config.allow_soft_placement = True
        sess = tf.Session(config=config)

        # Restore variables from disk.
        saver.restore(sess, MODEL_PATH)
        ops = {'pointclouds_pl': pointclouds_pl,
               'one_hot_vec_pl': one_hot_vec_pl,
               'labels_pl': labels_pl,
               'centers_pl': centers_pl,
               'heading_class_label_pl': heading_class_label_pl,
               'heading_residual_label_pl': heading_residual_label_pl,
               'size_class_label_pl': size_class_label_pl,
               'size_residual_label_pl': size_residual_label_pl,
               'is_training_pl': is_training_pl,
               'logits': end_points['mask_logits'],
               'center': end_points['center'],
               'end_points': end_points,
               'loss': loss}
        return sess, ops

def softmax(x):
    ''' Numpy function for softmax'''
    shape = x.shape
    probs = np.exp(x - np.max(x, axis=len(shape)-1, keepdims=True))
    probs /= np.sum(probs, axis=len(shape)-1, keepdims=True)
    return probs

def inference(sess, ops, pc, one_hot_vec, batch_size):
    ''' Run inference for frustum pointnets in batch mode '''
    assert pc.shape[0]%batch_size == 0

    num_batches = pc.shape[0]/batch_size
    logits = np.zeros((pc.shape[0], pc.shape[1], NUM_CLASSES))
    centers = np.zeros((pc.shape[0], 3))
    heading_logits = np.zeros((pc.shape[0], NUM_HEADING_BIN))
    heading_residuals = np.zeros((pc.shape[0], NUM_HEADING_BIN))
    size_logits = np.zeros((pc.shape[0], NUM_SIZE_CLUSTER))
    size_residuals = np.zeros((pc.shape[0], NUM_SIZE_CLUSTER, 3))
    scores = np.zeros((pc.shape[0],)) # 3D box score 
   
    ep = ops['end_points']
    #tf_profiler = model_analyzer.Profiler(graph=sess.graph)
    #run_options = tf.RunOptions(trace_level = tf.RunOptions.FULL_TRACE)
    #run_metadata = tf.RunMetadata()

    time_diff = 0
    for i in range(num_batches):
        feed_dict = {\
            ops['pointclouds_pl']: pc[i*batch_size:(i+1)*batch_size,...],
            ops['one_hot_vec_pl']: one_hot_vec[i*batch_size:(i+1)*batch_size,:],
            ops['is_training_pl']: False}

        print("real input:", pc[i*batch_size:(i+1)*batch_size,...].shape)

        start_time = timer()
        '''
        batch_logits, batch_centers, \
        batch_heading_scores, batch_heading_residuals, \
        batch_size_scores, batch_size_residuals = \
            sess.run([ops['logits'], ops['center'],
                ep['heading_scores'], ep['heading_residuals'],
                ep['size_scores'], ep['size_residuals']],
                feed_dict=feed_dict, options=run_options,
                run_metadata=run_metadata)
        '''
        batch_logits, batch_centers, \
        batch_heading_scores, batch_heading_residuals, \
        batch_size_scores, batch_size_residuals = \
            sess.run([ops['logits'], ops['center'],
                ep['heading_scores'], ep['heading_residuals'],
                ep['size_scores'], ep['size_residuals']],
                feed_dict=feed_dict)
        
        end_time = timer()
        time_diff += (end_time - start_time)

    '''
    fetched_timeline = timeline.Timeline(run_metadata.step_stats)
    chrome_trace = fetched_timeline.generate_chrome_trace_format()
    with open('timeline.json', 'w') as f: f.write(chrome_trace)
    '''
    return time_diff

def write_detection_results(result_dir, id_list, type_list, box2d_list, center_list, \
                            heading_cls_list, heading_res_list, \
                            size_cls_list, size_res_list, \
                            rot_angle_list, score_list):
    ''' Write frustum pointnets results to KITTI format label files. '''
    if result_dir is None: return
    results = {} # map from idx to list of strings, each string is a line (without \n)
    for i in range(len(center_list)):
        idx = id_list[i]
        output_str = type_list[i] + " -1 -1 -10 "
        box2d = box2d_list[i]
        output_str += "%f %f %f %f " % (box2d[0],box2d[1],box2d[2],box2d[3])
        h,w,l,tx,ty,tz,ry = provider.from_prediction_to_label_format(center_list[i],
            heading_cls_list[i], heading_res_list[i],
            size_cls_list[i], size_res_list[i], rot_angle_list[i])
        score = score_list[i]
        output_str += "%f %f %f %f %f %f %f %f" % (h,w,l,tx,ty,tz,ry,score)
        if idx not in results: results[idx] = []
        results[idx].append(output_str)

    # Write TXT files
    if not os.path.exists(result_dir): os.mkdir(result_dir)
    output_dir = os.path.join(result_dir, 'data')
    if not os.path.exists(output_dir): os.mkdir(output_dir)
    for idx in results:
        pred_filename = os.path.join(output_dir, '%06d.txt'%(idx))
        fout = open(pred_filename, 'w')
        for line in results[idx]:
            fout.write(line+'\n')
        fout.close() 

def fill_files(output_dir, to_fill_filename_list):
    ''' Create empty files if not exist for the filelist. '''
    for filename in to_fill_filename_list:
        filepath = os.path.join(output_dir, filename)
        if not os.path.exists(filepath):
            fout = open(filepath, 'w')
            fout.close()

def test_from_rgb_detection(output_filename, result_dir=None):
    ''' Test frustum pointents with 2D boxes from a RGB detector.
    Write test results to KITTI format label files.
    todo (rqi): support variable number of points.
    '''
    ps_list = []
    segp_list = []
    center_list = []
    heading_cls_list = []
    heading_res_list = []
    size_cls_list = []
    size_res_list = []
    rot_angle_list = []
    score_list = []
    onehot_list = []

    test_idxs = np.arange(0, len(TEST_DATASET))
    print(len(TEST_DATASET))
    batch_size = BATCH_SIZE
    num_batches = int((len(TEST_DATASET)+batch_size-1)/batch_size)
    total_time = 0.0
    profile_list = []
    time_list = []
    batch_data_to_feed = np.zeros((batch_size, NUM_POINT, NUM_CHANNEL))
    batch_one_hot_to_feed = np.zeros((batch_size, 3))
    sess, ops = get_session_and_ops(batch_size=batch_size, num_point=NUM_POINT)
    for batch_idx in range(RUN_SIZE):
        print('batch idx: %d' % (batch_idx))
        start_idx = batch_idx * batch_size
        end_idx = min(len(TEST_DATASET), (batch_idx+1) * batch_size)
        cur_batch_size = end_idx - start_idx

        batch_data, batch_rot_angle, batch_rgb_prob, batch_one_hot_vec = \
            get_batch(TEST_DATASET, test_idxs, start_idx, end_idx,
                NUM_POINT, NUM_CHANNEL, from_rgb_detection=True)
        
        print("batch data: ", batch_data.shape)    
        print("batch_one_hot_vec: ", batch_one_hot_vec.shape)    
        batch_data_to_feed[0:cur_batch_size,...] = batch_data
        batch_one_hot_to_feed[0:cur_batch_size,:] = batch_one_hot_vec

        # Run one batch inference
        time_diff = inference(sess, ops, batch_data_to_feed,
                batch_one_hot_to_feed, batch_size=batch_size)

        if (batch_idx < 3): continue
        print(time_diff)
        total_time += time_diff
        time_list.append(time_diff)
        '''
        profile = parse_timeline("timeline.json")
        tmp_list = dict2list(profile, pointnet_ops)
        profile_list.append(tmp_list)
        print(tmp_list)
        '''

    print('Avg. time:', statistics.mean(time_list))
    print('Time stddev: ', statistics.stdev(time_list))
    # Write detection results for KITTI evaluation

    avg_list = []
    dev_list = []
    for i in range(len(profile_list[0])):
        avg_list.append(statistics.mean([item[i] for item in profile_list]))
        dev_list.append(statistics.stdev([item[i] for item in profile_list]))

    print(avg_list)
    print(dev_list)


def test(output_filename, result_dir=None):
    ''' Test frustum pointnets with GT 2D boxes.
    Write test results to KITTI format label files.
    todo (rqi): support variable number of points.
    '''
    total_time = 0.0
    
    ps_list = []
    seg_list = []
    segp_list = []
    center_list = []
    heading_cls_list = []
    heading_res_list = []
    size_cls_list = []
    size_res_list = []
    rot_angle_list = []
    score_list = []

    test_idxs = np.arange(0, len(TEST_DATASET))
    batch_size = BATCH_SIZE
    num_batches = len(TEST_DATASET)/batch_size

    sess, ops = get_session_and_ops(batch_size=batch_size, num_point=NUM_POINT)
    correct_cnt = 0
    profile_list = []
    for batch_idx in range(RUN_SIZE):
        print('batch idx: %d' % (batch_idx))
        start_idx = batch_idx * batch_size
        end_idx = (batch_idx+1) * batch_size

        batch_data, batch_label, batch_center, \
        batch_hclass, batch_hres, batch_sclass, batch_sres, \
        batch_rot_angle, batch_one_hot_vec = \
            get_batch(TEST_DATASET, test_idxs, start_idx, end_idx,
                NUM_POINT, NUM_CHANNEL)

        print("batch_data: ", batch_data.shape)
        print("batch_one_hot_vec: ", batch_one_hot_vec.shape)

        #batch_output, batch_center_pred, \
        #batch_hclass_pred, batch_hres_pred, \
        #batch_sclass_pred, batch_sres_pred, batch_scores = \
        t1 = inference(sess, ops, batch_data, batch_one_hot_vec, batch_size=batch_size)

        if (batch_idx < 5): continue

        # total_time += (end_time - start_time)
        total_time += t1

    print("Avg time: ", total_time / RUN_SIZE)


if __name__=='__main__':
    if FLAGS.from_rgb_detection:
        print("?????")
        test_from_rgb_detection(FLAGS.output+'.pickle', FLAGS.output)
    else:
        test(FLAGS.output+'.pickle', FLAGS.output)
