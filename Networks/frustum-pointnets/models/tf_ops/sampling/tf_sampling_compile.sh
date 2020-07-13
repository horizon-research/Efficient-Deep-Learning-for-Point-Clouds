#/bin/bash
/usr/local/cuda/bin/nvcc tf_sampling_g.cu -o tf_sampling_g.cu.o -c -O2 -DGOOGLE_CUDA=1 -x cu -Xcompiler -fPIC

# TF1.2
# g++ -std=c++11 tf_sampling.cpp tf_sampling_g.cu.o \
# 	-o tf_sampling_so.so -shared -fPIC \
# 	-I /usr/local/lib/python2.7/dist-packages/tensorflow/include \
# 	-I /usr/local/cuda/include -lcudart \
# 	-L /usr/local/cuda/lib64/ -O2 # -D_GLIBCXX_USE_CXX11_ABI=0

CUDA_PATH=/usr/local/cuda
TF_INC=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())')
TF_LIB=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_lib())')

# TF1.4
g++ -std=c++11 tf_sampling.cpp tf_sampling_g.cu.o \
	-o tf_sampling_so.so -shared -fPIC \
	-I ${TF_INC} \
    -I ${CUDA_PATH}/include \
	-I ${TF_INC}/external/nsync/public -lcudart \
	-L ${CUDA_PATH}/lib64/ \
	-L ${TF_LIB} -ltensorflow_framework \
	-O2 -D_GLIBCXX_USE_CXX11_ABI=1
