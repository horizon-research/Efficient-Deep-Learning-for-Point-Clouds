### DGCNN
------------

### Prerequisite
### 1. Dataset
Currently, we only support the ModelNet40 benchmark used by the [original DGCNN project](https://github.com/WangYueFt/dgcnn). 
If you only want to experiment on this dataset, the ```modelnet_dataset.py``` script will take care of it; otherwise, we suggest following the [instructions](https://github.com/charlesq34/pointnet2#prepare-your-own-data) provided by the PointNet++ project.

### 2. Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 3.7 <br>
Libraries:
- Tensorflow 1.15.0 
- numpy 1.18
- cudnn 7.6.5

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### 3. Run:
This part is to run the inference on both the original network and the optimized network. <br>
0\. Switch to the ```dgcnn``` directory: <br>

1\. To run the **original version** of DGCNN (evaluation / inference): <br>
```python evaluate-baseline.py ``` <br>
To check out all the optional arguments for the inference, please run: <br>
```python evaluate-baseline.py -h```

2\. To run the **optimized version** of DGCNN (evaluation / inference): <br>
```python evaluate.py ``` <br>
To check out all the optional arguments for the inference, please run: <br>
```python evaluate.py -h```

3\. Check the results. After running as in step 1 and 2, it will print out the accuracy and latency: <br>
The original network: <br>

The optimized network: <br>

------------

### About
------------
