### DGCNN (Classification)

------------

For DGCNN (Segmentation), please check out [the part_seg directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn/part_seg).

### Prerequisite
### 1. Dataset
Currently, we only support the ModelNet40 benchmark used by the [original DGCNN project](https://github.com/WangYueFt/dgcnn). To download the dataset, run: 
```
python provider.py
``` 
If you want to experiment on other datasets, we suggest following the [instructions](https://github.com/charlesq34/pointnet2#prepare-your-own-data) provided by the PointNet++ project.



### 2. Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 3.7 <br>
Libraries:
- Tensorflow 1.15.0 
- numpy 1.18
- cudnn 7.6.5
- pillow 7.0.0

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### 3. Run:
This part is to run the inference on both the original network and the optimized network. <br>
0\. Switch to the ```dgcnn``` directory: <br>

1\. To run the **original version** of DGCNN (evaluation / inference): <br>
```
python evaluate-baseline.py 
```

To check out all the optional arguments, please run: <br>
```
python evaluate-baseline.py -h
```

2\. To run the **optimized version** of DGCNN (evaluation / inference): <br>
```
python evaluate.py 
```
To check out all the optional arguments, please run: <br>
```
python evaluate.py -h
```

3\. Check the results. After running as in step 1 and 2, it will print out the accuracy and latency: <br>
The original network: <br>
<img src="https://user-images.githubusercontent.com/19209239/83911018-8be16380-a739-11ea-9495-6bf7dfd10a00.png" alt="drawing" width="420"/>

The optimized network: <br>
<img src="https://user-images.githubusercontent.com/19209239/83911312-0d38f600-a73a-11ea-967f-cabf5c7092f1.png" alt="drawing" width="420"/>

------------

### About
------------
