import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Download dataset for point cloud part segmentation
DATASET_DIR = os.path.join(ROOT_DIR, '../../../Datasets/')
if not os.path.exists(DATASET_DIR):
    os.mkdir(DATASET_DIR)

if not os.path.exists(os.path.join(DATASET_DIR, 'PartAnnotation')):
    www = 'https://shapenet.cs.stanford.edu/ericyi/shapenetcore_partanno_v0.zip'
    zipfile = os.path.basename(www)
    os.system('cd %s; wget %s --no-check-certificate; unzip %s; rm %s' % (DATASET_DIR, www, zipfile, zipfile))

if not os.path.exists(os.path.join(DATASET_DIR, 'hdf5_data')):
    www = 'https://shapenet.cs.stanford.edu/media/shapenet_part_seg_hdf5_data.zip'
    zipfile = os.path.basename(www)
    os.system('cd %s; wget %s --no-check-certificate; unzip %s; rm %s' % (DATASET_DIR, www, zipfile, zipfile))
