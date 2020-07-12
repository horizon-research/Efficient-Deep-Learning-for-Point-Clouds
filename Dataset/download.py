'''
    This script is used to download and unzip datasets that shared by multiple networks.
'''

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default=None, help='Dataset named, use: --name ModelNet, --name ShapeNet')
FLAGS = parser.parse_args()

dataset = {}

# ModelNet40
dataset['ModelNet'] = ['modelnet40_ply_hdf5_2048', 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip']

# ShapeNet
dataset['ShapeNet'] = ['shapenetcore_partanno_segmentation_benchmark_v0_normal', 'https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip']

if not os.path.exists(os.path.join(dataset[FLAGS.name][0])):
    www = dataset[FLAGS.name][1]
    zipfile = os.path.basename(www)
    os.system("wget %s --no-check-certificate; unzip %s" %(www, zipfile))
    os.system("rm %s" %(zipfile))
