import os
import sys
import numpy as np
import h5py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Download dataset for point cloud classification
DATA_DIR = os.path.join(BASE_DIR, 'data')
if not os.path.exists(DATA_DIR):
  os.mkdir(DATA_DIR)
if not os.path.exists(os.path.join(DATA_DIR, 'modelnet40_ply_hdf5_2048')):
  www = 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip'
  zipfile = os.path.basename(www)
  os.system('wget %s; unzip %s' % (www, zipfile))
  os.system('mv %s %s' % (zipfile[:-4], DATA_DIR))
  os.system('rm %s' % (zipfile))


