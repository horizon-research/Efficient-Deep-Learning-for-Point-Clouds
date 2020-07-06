'''
    This script is used to compile and launch different network.
'''
import numpy as np
import argparse
import os
import sys
import statistics
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--run', type=str, default=None, help='Launch the model with default settings.')
parser.add_argument('--use_baseline', type=bool, default=False, help='Use baseline instead of efficient version.')
parser.add_argument('--use_limited', type=bool, default=False, help='Use limited aggr. instead of efficient version.')
FLAGS = parser.parse_args()

RUN_MODELS = {
    'pointnet2' : 'python evaluate.py',
    'frustum-pointnets' : 'bash scripts/command_test_v2.sh',
    'ldgcnn' : 'python evaluate.py --log_dir log_new --model_cnn ldgcnn',
    'dgcnn' : 'python evaluate.py'
}

RUN_BASELINES = {
    'pointnet2' : 'python evaluate-baseline.py',
    'frustum-pointnets' : 'bash scripts/command_test_v2_baselline.sh',
    'ldgcnn' : 'python evaluate.py --log_dir log_baseline --model_cnn ldgcnn_baseline',
    'dgcnn' : 'python evaluate-baseline.py'
}

RUN_LIMITED = {
    'pointnet2' : 'python evaluate-limited.py',
    'frustum-pointnets' : 'bash scripts/command_test_v2_limited.sh',
    'ldgcnn' : 'python evaluate.py --log_dir log_new --model_cnn ldgcnn',
    'dgcnn' : 'python evaluate.py'
}

dir_path = '../Networks/%s' % FLAGS.run
# Run some models
if FLAGS.run in RUN_MODELS and os.path.exists(dir_path):
    print('cd %s' % dir_path)
    ch_pid = os.fork()
    if ch_pid == 0:
        os.execlp('power', 'gpu', 'measured')
    else:
        if FLAGS.use_baseline:
            print('launching %s baseline' % FLAGS.run)
            os.system('cd %s; %s' % (dir_path, RUN_BASELINES[FLAGS.run]))
        elif FLAGS.use_limited:
            print('launching %s limited-aggr.' % FLAGS.run)
            os.system('cd %s; %s' % (dir_path, RUN_LIMITED[FLAGS.run]))
        else:
            print('launching %s efficient net' % FLAGS.run)
            os.system('cd %s; %s' % (dir_path, RUN_MODELS[FLAGS.run]))
        
        os.system('kill -9 %d' % ch_pid)
        number_file = open('measured_power.txt', 'r')
        nums = []
        for i in number_file.readlines():
            # assume power less than 1000 is idle
            if float(i) >= 1000:
                nums.append(float(i))

        print('Average power %f' % statistics.mean(nums))
        exit()
elif FLAGS.run is not None:
    print('[ERROR]: can\'t find the model %s to run.' % FLAGS.run)
    exit()

