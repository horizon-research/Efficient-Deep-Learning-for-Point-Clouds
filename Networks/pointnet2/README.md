### PointNet++
------------

### Prerequisite
### 1. Dataset
Currently, we only support the ModelNet benchmark used by the [original PointNet++ project](https://github.com/charlesq34/pointnet2). 
If you only want to experiment on ModelNet, the ```modelnet_dataset.py``` script will take care of it; otherwise, we suggest following the instructions [here](https://github.com/charlesq34/pointnet2#prepare-your-own-data).

### 2. Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries:
- Tensorflow 1.12.0 
- numpy 1.14
- CUDA 10.2
- cudnn 7.6.5
Toolchain:
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### 3. Compile:
0\.  Suppose we are in the ```pointnet2``` directory: <br>
1\.  Enter directory ```./tf_ops/3d_interpolation``` and check if the CUDA path in the ```tf_interpolate_compile.sh``` script is set correctly. If not, please correct. <br>
2\.  Run ```sh tf_interpolate_compile.sh``` <br>
3\.  Repeat 1-2 for ```./tf_ops/grouping``` and ```./tf_ops/sampling```. <br>
4\.  run 
```python compile.py``` 
to compile the [customized tf operators](https://github.com/charlesq34/pointnet2#compile-customized-tf-operators) (interpolation, grouping, sampling). 

### 4.

------------

### How to run

------------

### About
------------
