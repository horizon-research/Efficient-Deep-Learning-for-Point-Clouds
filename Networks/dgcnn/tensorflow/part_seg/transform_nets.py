import tensorflow as tf
import numpy as np
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, '../utils'))
import tf_util

def input_transform_net(edge_feature, nn_idx, k, is_training, bn_decay=None, K=3, is_dist=False):
  """ Input (XYZ) Transform Net, input is BxNx3 gray image
    Return:
      Transformation matrix of size 3xK """

  # edge_feature here: point clouds

  batch_size = edge_feature.get_shape()[0].value
  num_point = edge_feature.get_shape()[1].value
  print("(transform net) input", edge_feature.shape)
  print("(transform net) input to conv2d", edge_feature.shape)
  
  edge_feature = tf.expand_dims(edge_feature, axis=-2)
  print("edge_feature: ", edge_feature.shape)

  # input_image = tf.expand_dims(point_cloud, -1)
  net = tf_util.conv2d(edge_feature, 64, [1,1],
             padding='VALID', stride=[1,1],
             bn=True, is_training=is_training,
             scope='tconv1', bn_decay=bn_decay, is_dist=is_dist)
  print("(transform net) output of conv2d", net.shape)

  net = tf_util.conv2d(net, 128, [1,1],
             padding='VALID', stride=[1,1],
             bn=True, is_training=is_training,
             scope='tconv2', bn_decay=bn_decay, is_dist=is_dist)
  print("(transform net) output of conv2d", net.shape)
 
  with tf.name_scope("group1"):
      # group
      net_expanded = net
          
      point_cloud_shape = net.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value

      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1]) 

      # neighborhoods
      net = tf.squeeze(net, [2])
      net = tf.reshape(net, [-1, num_dims])
      print("idx_: ", idx_.shape)
      print("net: ", net.shape)
      net_neighbors = tf.gather(net, nn_idx+idx_, name="nn_group1")
      print("net_neighbors: ", net_neighbors.shape)
      '''      
      # centroids
      net_central = tf.tile(net_expanded, [1, 1, k, 1])
      # correction
      net = net_neighbors - net_central
      print("corrected feature: ", net.shape)
      '''
  net = tf.reduce_max(net_neighbors, axis=-2, keep_dims=True)
  print("(transform net) output of reduce_max", net.shape)
  
  net = net - net_expanded
  net = tf.concat([net_expanded,net], axis=-1)

  print("------------------", net.shape)
  net = tf_util.conv2d(net, 1024, [1,1],
             padding='VALID', stride=[1,1],
             bn=True, is_training=is_training,
             scope='tconv3', bn_decay=bn_decay, is_dist=is_dist) 
  print("(transform net) output of conv2d", net.shape)

  net = tf_util.max_pool2d(net, [num_point,1],
               padding='VALID', scope='tmaxpool')
  print("(transform net) output of max", net.shape)

  net = tf.reshape(net, [batch_size, -1])
  print("(transform net) reshape output", net.shape)

  net = tf_util.fully_connected(net, 512, bn=True, is_training=is_training,
                  scope='tfc1', bn_decay=bn_decay,is_dist=is_dist)
  print("(transform net) fc1 output", net.shape)

  net = tf_util.fully_connected(net, 256, bn=True, is_training=is_training,
                  scope='tfc2', bn_decay=bn_decay,is_dist=is_dist)
  print("(transform net) fc2 output", net.shape)

  with tf.variable_scope('transform_XYZ') as sc:
    # assert(K==3)
    with tf.device('/cpu:0'):
      weights = tf.get_variable('weights', [256, K*K],
                    initializer=tf.constant_initializer(0.0),
                    dtype=tf.float32)
      biases = tf.get_variable('biases', [K*K],
                   initializer=tf.constant_initializer(0.0),
                   dtype=tf.float32)
    biases += tf.constant(np.eye(K).flatten(), dtype=tf.float32)
    print("(transform net) matmul(net, weights):")
    print("(transform net) net:", net.shape)
    print("(transform net) weights:", weights.shape)

    transform = tf.matmul(net, weights)
    print("(transform net) transform", transform.shape)
    transform = tf.nn.bias_add(transform, biases)
    print("(transform net) transform", transform.shape)

  transform = tf.reshape(transform, [batch_size, K, K])
  return transform
