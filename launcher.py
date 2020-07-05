'''
    This script is used to compile and launch different network.
'''
import numpy as np
import argparse
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--compile', type=str, default=None, help='Compile libraries in the models, to compile a specific network, use: --compile [NETWORK_NAME] or to copmpile all models using, --compile all')
parser.add_argument('--download', type=str, default=None, help='Download the specific dataset for the models, to download a dataset for a specific network, use: --compile [NETWORK_NAME] or to copmpile all models using, --compile all')
parser.add_argument('--list_models', help='List all model names.')
parser.add_argument('--run', type=str, default=None, help='Launch the model with default settings.')
parser.add_argument('--train', type=str, default=None, help='Train the model with default settings.')
parser.add_argument('--use_baseline', type=bool, default=False, help='Use baseline instead of efficient version.')
parser.add_argument('--use_limited', type=bool, default=False, help='Use limited aggr. instead of efficient version.')
FLAGS = parser.parse_args()

COMPILE_MODELS = ['pointnet2', 'frustum-pointnets']

# Compile necessary modules
if FLAGS.compile == 'all':
    for m in COMPILE_MODELS:
        dir_path = './Networks/%s' % m
        if os.path.exists(dir_path):
            print('cd %s' % dir_path)
            os.system('cd %s; python compile.py' % dir_path)
        else:
            print('[ERROR]: can\'t find the path %s' % dir_path)
    exit()
elif FLAGS.compile in COMPILE_MODELS:
    dir_path = './Networks/%s' % FLAGS.compile
    if os.path.exists(dir_path):
        print('cd %s' % dir_path)
        os.system('cd %s; python compile.py' % dir_path)
    else:
        print('[ERROR]: can\'t find the path %s' % dir_path)
    exit()
elif FLAGS.compile is not None:
    print('[ERROR]: can\'t find the model %s to compile.' % FLAGS.compile)
    exit()

DOWNLOAD_SCRIPTS = {
    'pointnet2' : 'modelnet_h5_dataset.py',
    'frustum-pointnets' : 'download_dataset.py',
    'ldgcnn' : 'download_modelnet.py',
    'dgcnn' : 'provider.py',
}

if FLAGS.download == 'all':
    for key in DOWNLOAD_SCRIPTS:
        dir_path = './Networks/%s' % key
        if os.path.exists(dir_path):
            print('run %s/%s' % (dir_path, DOWNLOAD_SCRIPTS[key]))
            os.system('cd %s; python %s' % dir_path, DOWNLOAD_SCRIPTS[key])
        else:
            print('[ERROR]: can\'t find the path %s' % dir_path)
    exit()
elif FLAGS.download in COMPILE_MODELS:
    dir_path = './Networks/%s' % FLAGS.download
    if os.path.exists(dir_path):
        print('cd %s' % dir_path)
        os.system('cd %s; python %s' % (dir_path, DOWNLOAD_SCRIPTS[key]))
    else:
        print('[ERROR]: can\'t find the path %s' % dir_path)
    exit()
elif FLAGS.download is not None:
    print('[ERROR]: can\'t find the model %s\'s dataset to download.' % FLAGS.download)
    exit()

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

dir_path = './Networks/%s' % FLAGS.run
# Run some models
if FLAGS.run in RUN_MODELS and os.path.exists(dir_path):
    print('cd %s' % dir_path)
    if FLAGS.use_baseline:
        print('launching %s baseline' % FLAGS.run)
        os.system('cd %s; %s' % (dir_path, RUN_BASELINES[FLAGS.run]))
    elif FLAGS.use_limited:
        print('launching %s limited-aggr.' % FLAGS.run)
        os.system('cd %s; %s' % (dir_path, RUN_LIMITED[FLAGS.run]))
    else:
        print('launching %s efficient net' % FLAGS.run)
        os.system('cd %s; %s' % (dir_path, RUN_MODELS[FLAGS.run]))
    exit()
elif FLAGS.run is not None:
    print('[ERROR]: can\'t find the model %s to run.' % FLAGS.run)
    exit()

