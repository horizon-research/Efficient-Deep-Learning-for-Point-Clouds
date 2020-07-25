# TF1.4
#/bin/bash
if [ ! $1 ]; then
    CUDA_PATH='/usr/local/cuda-10.2'
else
    CUDA_PATH=$1
fi

#CUDA_PATH=$1
TF_INC=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())')
TF_LIB=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_lib())')
g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -fPIC -I $TF_INC -I $CUDA_PATH/include -lcudart -L $CUDA_PATH/lib64/ -L$TF_LIB -I$TF_INC/external/nsync/public -ltensorflow_framework  -O2 #-D_GLIBCXX_USE_CXX11_ABI=0
