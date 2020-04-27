import tensorflow as tf

#import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior() 
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False
import numpy as np
import math
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, '../utils'))
sys.path.append(os.path.join(BASE_DIR, '../../utils'))
import tf_util
from transform_nets import input_transform_net

def print(*args):
    return

def placeholder_inputs(batch_size, num_point):
    pointclouds_pl = tf.placeholder(tf.float32, shape=(batch_size, num_point, 3))
    labels_pl = tf.placeholder(tf.int32, shape=(batch_size))
    return pointclouds_pl, labels_pl

def get_model(point_cloud, is_training, bn_decay=None):
  """ Classification PointNet, input is BxNx3, output Bx40 """
  batch_size = point_cloud.get_shape()[0].value
  num_point = point_cloud.get_shape()[1].value
  end_points = {}
  k = 20

  print("--------------------------------------------------------------------\nm0")
  with tf.name_scope("pc_trans"):
      print("(get_model) input point_cloud:", point_cloud.shape)
      adj_matrix = tf_util.pairwise_distance(point_cloud)
      print("(get_model) construct adj_matrix:", adj_matrix.shape)
      nn_idx = tf_util.knn(adj_matrix, k=k)
      print("(get_model) knn:", nn_idx.shape)
      # edge_feature = tf_util.get_edge_feature(point_cloud, nn_idx=nn_idx, k=k) 
  print("--------------------------------------------------------------------")

  #with tf.name_scope('transform_net1'):
  with tf.variable_scope('transform_net1') as sc:
    transform = input_transform_net(point_cloud, nn_idx, k, is_training, bn_decay, K=3)
  print("(get_model) output of transform net: transform:", transform.shape)
  with tf.name_scope('init_t'):
    point_cloud_transformed = tf.matmul(point_cloud, transform)

  print("--------------------------------------------------------------------\nm1")
  with tf.name_scope("pc_m1"):    
      print("(get_model) point_cloud_transformed (input to distance calculcation):", point_cloud_transformed.shape)
      adj_matrix = tf_util.pairwise_distance(point_cloud_transformed)
      print("(get_model) adj matrix:", adj_matrix.shape)
      nn_idx = tf_util.knn(adj_matrix, k=k)
      print("(get_model) nn_idx:", nn_idx.shape)
      # edge_feature = tf_util.get_edge_feature(point_cloud_transformed, nn_idx=nn_idx, k=k)
      
  point_cloud_transformed = tf.expand_dims(point_cloud_transformed, axis=-2)
  print("point cloud transformed: ", point_cloud_transformed.shape)
  
  net = tf_util.conv2d(point_cloud_transformed, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='dgcnn1', bn_decay=bn_decay)
  print("(get_model) conv2d output:", net.shape)
   
  with tf.name_scope("pc_m1_group"):
      # group 
      net_expanded = net
      
      point_cloud_shape = net.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value

      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      net = tf.squeeze(net, [2])
      net = tf.reshape(net, [-1, num_dims])    
      net_neighbors = tf.gather(net, nn_idx+idx_)

  net = tf.reduce_max(net_neighbors, axis=-2, keep_dims=True)
  net = net - net_expanded
  print("correction")
  net = tf.concat([net_expanded, net], axis=-1)
  print("concat:", net.shape)
  
  net1 = net
  
  print("--------------------------------------------------------------------\nm2")
  with tf.name_scope("pc_m2"):
      adj_matrix = tf_util.pairwise_distance(net)
      print("(get_model) adj matrix:", adj_matrix.shape)
      nn_idx = tf_util.knn(adj_matrix, k=k)
      print("(get_model) nn_idx:", nn_idx.shape)      
      #edge_feature = tf_util.get_edge_feature(net, nn_idx=nn_idx, k=k)
      #print("(get_model) edge_feature:", edge_feature.shape)

  print("(get_model) conv2d")
  print("(get_model) conv2d input:", net.shape)
  net = tf_util.conv2d(net, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='dgcnn2', bn_decay=bn_decay)
  print("(get_model) conv2d output:", net.shape)

  with tf.name_scope("pc_m2_group"):
      # group 
      print("(get_model) group m2:")
      net_expanded = net
      
      point_cloud_shape = net.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value

      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      net = tf.squeeze(net, [2])
      net = tf.reshape(net, [-1, num_dims])
      print("net", net.shape)
      net_neighbors = tf.gather(net, nn_idx+idx_)
      print("net_neighbors", net_neighbors.shape)

  net = tf.reduce_max(net_neighbors, axis=-2, keep_dims=True)
  net = net - net_expanded
  print("correction")

  print("(get_model) maxpooling output:", net.shape)
  net = tf.concat([net_expanded, net], axis=-1)
  print("concat:", net.shape) 
  net2 = net

  print("--------------------------------------------------------------------\nm3")
  with tf.name_scope("pc_m3"):
      adj_matrix = tf_util.pairwise_distance(net)
      print("(get_model) adj matrix:", adj_matrix.shape)
      nn_idx = tf_util.knn(adj_matrix, k=k)
      print("(get_model) nn_idx:", nn_idx.shape)
      
      # edge_feature = tf_util.get_edge_feature(net, nn_idx=nn_idx, k=k)  

  print("(get_model) conv2d")
  net = tf_util.conv2d(net, 64, [1,1], 
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, 
                       scope='dgcnn3', bn_decay=bn_decay)
  print("(get_model) conv2d output:", net.shape)
  
  with tf.name_scope("pc_m3_group"):
      # group 
      print("(get_model) group m3:")
      net_expanded = net
      
      point_cloud_shape = net.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value

      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      net = tf.squeeze(net, [2])
      net = tf.reshape(net, [-1, num_dims])
      
      net_neighbors = tf.gather(net, nn_idx+idx_)

  net = tf.reduce_max(net_neighbors, axis=-2, keep_dims=True)
  print("(get_model) maxpooling output:", net.shape)
  net = net - net_expanded
  print("correction")
  net = tf.concat([net_expanded, net], axis=-1)
  print("concat:", net.shape)  
  net3 = net

  print("--------------------------------------------------------------------\nm4")
  with tf.name_scope("pc_m4"):
      adj_matrix = tf_util.pairwise_distance(net)
      print("(get_model) adj matrix:", adj_matrix.shape)
      nn_idx = tf_util.knn(adj_matrix, k=k)
      print("(get_model) nn_idx:", nn_idx.shape)
      # edge_feature = tf_util.get_edge_feature(net, nn_idx=nn_idx, k=k)  
  
  print("(get_model) conv2d")
  net = tf_util.conv2d(net, 128, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='dgcnn4', bn_decay=bn_decay)
  
  with tf.name_scope("pc_m4_group"):
      # group 
      net_expanded = net
      
      point_cloud_shape = net.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value

      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      net = tf.squeeze(net, [2])
      net = tf.reshape(net, [-1, num_dims])
      
      net_neighbors = tf.gather(net, nn_idx+idx_)
      print("net_neighbors", net_neighbors.shape)

  net = tf.reduce_max(net_neighbors, axis=-2, keep_dims=True)
  print("(get_model) max output:", net.shape)
  net = net - net_expanded
  print("correction")
  net = tf.concat([net_expanded, net], axis=-1)
  print("concat:", net.shape)

  net4 = net

  print("--------------------------------------------------------------------\nm5")
  print("(get_model) agg conv:")
  concat = tf.concat([net1, net2, net3, net4], axis=-1)
  print("(get_model) agg output:", concat.shape)
  net = tf_util.conv2d(concat, 1024, [1, 1], 
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='agg', bn_decay=bn_decay)
  print("(get_model) agg conv output:", net.shape)
  net = tf.reduce_max(net, axis=1, keep_dims=True) 
  print("(get_model) max output:", net.shape)

  print("--------------------------------------------------------------------\nm6")
  # MLP on global point cloud vector
  net = tf.reshape(net, [batch_size, -1]) 
  net = tf_util.fully_connected(net, 512, bn=True, is_training=is_training,
                                scope='fc1', bn_decay=bn_decay)
  print("(get_model) fc1 output:", net.shape)
  net = tf_util.dropout(net, keep_prob=0.5, is_training=is_training,
                         scope='dp1')
  net = tf_util.fully_connected(net, 256, bn=True, is_training=is_training,
                                scope='fc2', bn_decay=bn_decay)
  print("(get_model) fc2 output:", net.shape)
  net = tf_util.dropout(net, keep_prob=0.5, is_training=is_training,
                        scope='dp2')
  net = tf_util.fully_connected(net, 40, activation_fn=None, scope='fc3')
  print("(get_model) fc3 output:", net.shape)

  return net, end_points

def get_loss(pred, label, end_points):
  """ pred: B*NUM_CLASSES,
      label: B, """
  labels = tf.one_hot(indices=label, depth=40)
  loss = tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=pred, label_smoothing=0.2)
  classify_loss = tf.reduce_mean(loss)
  return classify_loss


if __name__=='__main__':
  batch_size = 32
  num_pt = 1024
  pos_dim = 3

  input_feed = np.random.rand(batch_size, num_pt, pos_dim)
  label_feed = np.random.rand(batch_size)
  label_feed[label_feed>=0.5] = 1
  label_feed[label_feed<0.5] = 0
  label_feed = label_feed.astype(np.int32)

  # # np.save('./debug/input_feed.npy', input_feed)
  # input_feed = np.load('./debug/input_feed.npy')
  # print input_feed

  with tf.Graph().as_default():
    input_pl, label_pl = placeholder_inputs(batch_size, num_pt)
    pos, ftr = get_model(input_pl, tf.constant(True))
    # loss = get_loss(logits, label_pl, None)

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.allow_soft_placement = True
    config.log_device_placement = False
    sess = tf.Session(config=config)

    #with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    feed_dict = {input_pl: input_feed, label_pl: label_feed}
    res1, res2 = sess.run([pos, ftr], feed_dict=feed_dict)
    #print(res1.shape)
    #print(res1)
