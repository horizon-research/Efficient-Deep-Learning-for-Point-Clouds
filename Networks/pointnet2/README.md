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

Compiler Toolchain: 
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### 3. Compile:
This part is to compile the [customized tf operators](https://github.com/charlesq34/pointnet2#compile-customized-tf-operators) (interpolation, grouping, sampling). Please follow the steps below.<br>
0\. Suppose we are in the ```pointnet2``` directory: <br>
<img src="https://user-images.githubusercontent.com/19209239/83693739-a7772d80-a5c4-11ea-8459-f0e6841f29e8.png" alt="drawing" width="600"/>

1\. Enter directory ```./tf_ops/3d_interpolation``` and check if the CUDA path in the ```tf_interpolate_compile.sh``` script is set correctly; if not, please correct: <br>
<img src="https://user-images.githubusercontent.com/19209239/83694347-d8a42d80-a5c5-11ea-850c-261019637fa2.png" alt="drawing" width="1000"/>

2\. Run ```sh tf_interpolate_compile.sh```.<br>
3\. Repeat 1-2 for ```./tf_ops/grouping``` and ```./tf_ops/sampling```. <br><br>
Or, if the CUDA paths are already set correctly, run 
```python compile.py``` in the ```pointnet2``` directory. 

### 4. Run:
This part is to run the inference on both the original network and the optimized network. <br>
0\. Switch to the ```pointnet2``` directory: <br>
<img src="https://user-images.githubusercontent.com/19209239/83693739-a7772d80-a5c4-11ea-8459-f0e6841f29e8.png" alt="drawing" width="600"/>

1\. To run the **original version** of PointNet++ (evaluation / inference): <br>
```python evaluate-baseline.py ``` <br>
To check out all the optional arguments for the inference, please run: <br>
```python evaluate-baseline.py -h```

2\. To run the **optimized version** of PointNet++ (evaluation / inference): <br>
```python evaluate.py ``` <br>
To check out all the optional arguments for the inference, please run: <br>
```python evaluate.py -h```

3\. Check the results. After running as in step 1 and 2, it will print out the accuracy and latency: <br>
The original network: <br>
<img src="https://user-images.githubusercontent.com/19209239/83704360-ebc3f700-a5df-11ea-8dcb-b842e0a85f30.png" alt="drawing" width="580"/>

The optimized network: <br>
<img src="https://user-images.githubusercontent.com/19209239/83761562-7cccb980-a644-11ea-976b-6438875ebc70.png" alt="drawing" width="620"/>

------------

### About
------------
