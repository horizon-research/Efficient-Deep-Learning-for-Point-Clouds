### DGCNN (Segmentation)
------------

### Prerequisite
### 1. Dataset
Currently, we only support the ShapeNet benchmark used by the [original DGCNN project](https://github.com/WangYueFt/dgcnn/tree/master/tensorflow/part_seg). To download the dataset, please run: <br>
```
sh +x download_data.sh
```

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
python test-baseline.py 
```

To check out all the optional arguments for the inference, please run: <br>
```
python test-baseline.py -h
```

2\. To run the **optimized version** of DGCNN (evaluation / inference): <br>
```
python test.py 
```

To check out all the optional arguments for the inference, please run: <br>
```
python test.py -h
```

3\. Check the results. After running as in step 1 and 2, it will print out the accuracy and latency: <br>
The original network: <br>
<img src="" alt="drawing" width="420"/>

The optimized network: <br>
<img src="" alt="drawing" width="420"/>

------------

### About
------------
