import tensorflow as tf
import numpy as np
import math
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))
sys.path.append(os.path.join(BASE_DIR, '../utils'))
sys.path.append(os.path.join(BASE_DIR, '../models'))
sys.path.append(os.path.join(BASE_DIR, '../'))
import tf_util
from transform_nets import input_transform_net

def print(*args):
    return

def get_model(point_cloud, input_label, is_training, cat_num, part_num, \
    batch_size, num_point, weight_decay, bn_decay=None):

  batch_size = point_cloud.get_shape()[0].value
  num_point = point_cloud.get_shape()[1].value
  input_image = tf.expand_dims(point_cloud, -1)

  k = 20

  adj = tf_util.pairwise_distance(point_cloud)
  nn_idx = tf_util.knn(adj, k=k)
  # edge_feature = tf_util.get_edge_feature(input_image, nn_idx=nn_idx, k=k)

  with tf.variable_scope('transform_net1') as sc:
    transform = input_transform_net(point_cloud, nn_idx, k, is_training, bn_decay, K=3, is_dist=True)
  point_cloud_transformed = tf.matmul(point_cloud, transform)
  
  input_image = tf.expand_dims(point_cloud_transformed, -2)
  print("input_image:", input_image.shape)

  with tf.name_scope("pc_m1"):
    adj = tf_util.pairwise_distance(point_cloud_transformed)
    nn_idx = tf_util.knn(adj, k=k)
    # edge_feature = tf_util.get_edge_feature(input_image, nn_idx=nn_idx, k=k)

  out1 = tf_util.conv2d(input_image, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, weight_decay=weight_decay,
                       scope='adj_conv1', bn_decay=bn_decay, is_dist=True)
  
  out2 = tf_util.conv2d(out1, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, weight_decay=weight_decay,
                       scope='adj_conv2', bn_decay=bn_decay, is_dist=True)
  print("out2:", out2.shape)

  with tf.name_scope("pc_m1_group"):
      print("pc_m1_group")
      out_expanded = out2

      point_cloud_shape = out2.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value
      
      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighbors
      out2 = tf.squeeze(out2, [2])
      out2 = tf.reshape(out2, [-1, num_dims])
      print("out2", out2.shape)

      out2_neighbors = tf.gather(out2, nn_idx+idx_)
      print("out2_neighbors: ", out2_neighbors.shape) 
  
  net_1 = tf.reduce_max(out2_neighbors, axis=-2, keep_dims=True)
  print("net_1:", net_1.shape)
  
  # correction
  net_1 = net_1 - out_expanded
  print("net_1: ", net_1.shape) 
  
  # concat
  net_1 = tf.concat([out_expanded, net_1], axis=-1)
  print("net_1: ", net_1.shape) 

  with tf.name_scope("pc_m2"):
    adj = tf_util.pairwise_distance(net_1)
    nn_idx = tf_util.knn(adj, k=k)
    # edge_feature = tf_util.get_edge_feature(net_1, nn_idx=nn_idx, k=k)

  out3 = tf_util.conv2d(net_1, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, weight_decay=weight_decay,
                       scope='adj_conv3', bn_decay=bn_decay, is_dist=True)

  out4 = tf_util.conv2d(out3, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, weight_decay=weight_decay,
                       scope='adj_conv4', bn_decay=bn_decay, is_dist=True)

  with tf.name_scope("pc_m2_group"):
      # group
      print("pc_m2_group")
      out_expanded = out4

      point_cloud_shape = out4.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value
      
      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      out4 = tf.squeeze(out4, [2])
      out4 = tf.reshape(out4, [-1, num_dims])
      print("out4", out4.shape)

      # neighbors
      out4_neighbors = tf.gather(out4, nn_idx+idx_)
      print("out4_neighbors: ", out4_neighbors.shape)

  net_2 = tf.reduce_max(out4_neighbors, axis=-2, keep_dims=True)
 
  # correction
  net_2 = net_2 - out_expanded
  print("net_2: ", net_2.shape)

  # concat
  net_2 = tf.concat([out_expanded, net_2], axis=-1)
  print("net_2: ",net_2.shape)

  with tf.name_scope("pc_m3"): 
    adj = tf_util.pairwise_distance(net_2)
    nn_idx = tf_util.knn(adj, k=k)
    # edge_feature = tf_util.get_edge_feature(net_2, nn_idx=nn_idx, k=k)

  out5 = tf_util.conv2d(net_2, 64, [1,1],
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training, weight_decay=weight_decay,
                       scope='adj_conv5', bn_decay=bn_decay, is_dist=True)

  # out6 = tf_util.conv2d(out5, 64, [1,1],
  #                      padding='VALID', stride=[1,1],
  #                      bn=True, is_training=is_training, weight_decay=weight_decay,
  #                      scope='adj_conv6', bn_decay=bn_decay, is_dist=True)


  with tf.name_scope("pc_m3_group"):
      print("pc_m3_group")
      out_expanded = out5

      point_cloud_shape = out5.get_shape()
      batch_size = point_cloud_shape[0].value
      num_points = point_cloud_shape[1].value
      num_dims = point_cloud_shape[-1].value
      
      idx_ = tf.range(batch_size) * num_points
      idx_ = tf.reshape(idx_, [batch_size, 1, 1])

      # neighborhood
      out5 = tf.squeeze(out5, [2])
      out5 = tf.reshape(out5, [-1, num_dims])
      print("out5", out5.shape)

      # neighbors
      out5_neighbors = tf.gather(out5, nn_idx+idx_)
      print("out5_neighbors: ", out5_neighbors.shape)

  net_3 = tf.reduce_max(out5_neighbors, axis=-2, keep_dims=True)

  # correction
  net_3 = net_3 - out_expanded
  print("net_3: ", net_3.shape)

  # concat
  net_3 = tf.concat([out_expanded, net_3], axis=-1)

  out7 = tf_util.conv2d(tf.concat([net_1, net_2, net_3], axis=-1), 1024, [1, 1], 
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='adj_conv7', bn_decay=bn_decay, is_dist=True)

  out_max = tf_util.max_pool2d(out7, [num_point, 1], padding='VALID', scope='maxpool')


  one_hot_label_expand = tf.reshape(input_label, [batch_size, 1, 1, cat_num])
  one_hot_label_expand = tf_util.conv2d(one_hot_label_expand, 64, [1, 1], 
                       padding='VALID', stride=[1,1],
                       bn=True, is_training=is_training,
                       scope='one_hot_label_expand', bn_decay=bn_decay, is_dist=True)
  out_max = tf.concat(axis=3, values=[out_max, one_hot_label_expand])
  expand = tf.tile(out_max, [1, num_point, 1, 1])

  concat = tf.concat(axis=3, values=[expand, 
                                     net_1,
                                     net_2,
                                     net_3])

  net2 = tf_util.conv2d(concat, 256, [1,1], padding='VALID', stride=[1,1], bn_decay=bn_decay,
            bn=True, is_training=is_training, scope='seg/conv1', weight_decay=weight_decay, is_dist=True)
  net2 = tf_util.dropout(net2, keep_prob=0.6, is_training=is_training, scope='seg/dp1')
  net2 = tf_util.conv2d(net2, 256, [1,1], padding='VALID', stride=[1,1], bn_decay=bn_decay,
            bn=True, is_training=is_training, scope='seg/conv2', weight_decay=weight_decay, is_dist=True)
  net2 = tf_util.dropout(net2, keep_prob=0.6, is_training=is_training, scope='seg/dp2')
  net2 = tf_util.conv2d(net2, 128, [1,1], padding='VALID', stride=[1,1], bn_decay=bn_decay,
            bn=True, is_training=is_training, scope='seg/conv3', weight_decay=weight_decay, is_dist=True)
  net2 = tf_util.conv2d(net2, part_num, [1,1], padding='VALID', stride=[1,1], activation_fn=None, 
            bn=False, scope='seg/conv4', weight_decay=weight_decay, is_dist=True)

  net2 = tf.reshape(net2, [batch_size, num_point, part_num])

  return net2


def get_loss(seg_pred, seg):
  per_instance_seg_loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=seg_pred, labels=seg), axis=1)
  seg_loss = tf.reduce_mean(per_instance_seg_loss)
  per_instance_seg_pred_res = tf.argmax(seg_pred, 2)
  
  return seg_loss, per_instance_seg_loss, per_instance_seg_pred_res

