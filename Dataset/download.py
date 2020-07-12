import os
import sys

dataset = {}

# ModelNet40
dataset['ModelNet'] = ['modelnet40_ply_hdf5_2048', 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip']

# ShapeNet
dataset['ShapeNet'] = ['shapenetcore_partanno_segmentation_benchmark_v0_normal', 'https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip']

name = sys.argv[1]

if not os.path.exists(os.path.join(dataset[name][0])):
    www = dataset[name][1]
    zipfile = os.path.basename(www)
    os.system("wget %s --no-check-certificate; unzip %s" %(www, zipfile))
    os.system("rm %s" %(zipfile))
