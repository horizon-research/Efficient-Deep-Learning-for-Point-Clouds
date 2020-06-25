import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Download dataset for point cloud classification
DATA_DIR = os.path.join(BASE_DIR, 'kitti')
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
    
www = 'https://shapenet.cs.stanford.edu/media/frustum_data.zip'
zipfile = os.path.basename(www)
os.system('wget %s; unzip %s' % (www, zipfile))
os.system('mv %s/*.pickle %s' % (zipfile[:-4], DATA_DIR))
os.system('rm %s' % (zipfile))
os.system('rm -r %s' % (zipfile[:-4]))

