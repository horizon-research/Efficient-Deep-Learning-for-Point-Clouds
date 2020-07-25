import os 

CUDA_PATH = '/usr/local/cuda-10.2'

print("compiling: tf_interpolate_compile")
os.system('cd ./tf_ops/3d_interpolation; sh tf_interpolate_compile.sh %s' % (CUDA_PATH))
print("done")

print("compiling: tf_grouping_compile")
os.system('cd ./tf_ops/grouping; sh tf_grouping_compile.sh %s' % (CUDA_PATH))
print("done")

print("compiling: tf_sampling_compile")
os.system('cd ./tf_ops/sampling/; sh tf_sampling_compile.sh %s' % (CUDA_PATH))
print("done")

