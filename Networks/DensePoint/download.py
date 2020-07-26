import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Download dataset for point cloud classification
DATASET_DIR = os.path.join(ROOT_DIR, '../../Datasets/')
if not os.path.exists(DATASET_DIR):
    os.mkdir(DATASET_DIR)

if not os.path.exists(os.path.join(DATASET_DIR, 'modelnet40_ply_hdf5_2048')):
    www = 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip'
    zipfile = os.path.basename(www)
    os.system('cd %s; wget %s --no-check-certificate; unzip %s; rm %s' % (DATASET_DIR, www, zipfile, zipfile))
