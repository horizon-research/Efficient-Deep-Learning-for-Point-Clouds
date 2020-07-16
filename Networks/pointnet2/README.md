### PointNet++ (Classification)
------------

For PointNet++ (Segmentation), please check out the [part_seg](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2/part_seg) directory.

---

### Dataset
Currently, we only support the ModelNet benchmark used by the [original PointNet++ project](https://github.com/charlesq34/pointnet2). To download the dataset, run: 
```
python modelnet_h5_dataset.py
``` 
If you want to experiment on your own dataset, we suggest following the instructions [here](https://github.com/charlesq34/pointnet2#prepare-your-own-data).

---

### Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries: Tensorflow 1.12.0, numpy 1.14, CUDA 10.2, cudnn 7.6.5

Compiler Toolchain: 
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

---

### Installation
Instructions on how to compile the [customized tf operators](https://github.com/charlesq34/pointnet2#compile-customized-tf-operators) (interpolation, grouping, sampling). Please follow the steps below.<br>
0\. Suppose we are in the ```pointnet2``` directory: <br>
<img src="https://user-images.githubusercontent.com/19209239/83693739-a7772d80-a5c4-11ea-8459-f0e6841f29e8.png" alt="drawing" width="600"/>

1\. Enter directory ```./tf_ops/3d_interpolation``` and check if the CUDA path in the ```tf_interpolate_compile.sh``` script is set correctly; if not, please set that to the CUDA path on your machine (usually it's under /usr/local/). <br>
<img src="https://user-images.githubusercontent.com/19209239/83694347-d8a42d80-a5c5-11ea-850c-261019637fa2.png" alt="drawing" width="800"/>

2\. Run ```sh tf_interpolate_compile.sh```.<br>
3\. Repeat 1-2 for ```./tf_ops/grouping``` and ```./tf_ops/sampling```. <br>

If the CUDA paths are already set correctly, you can run 
```python compile.py``` in the ```pointnet2``` directory instead of following the 3 steps above.

---

### Training

---

### Evaluation
There are three versions of PointNet++ (cls): <br>
**Baseline**: the original PointNet++ (cls) with implementation optimizations. <br>
**Limited Delayed-Aggregation**: the version with limited delayed-ggregation optimization. <br>
**Delayed-Aggregation**: the version with full delayed-aggregation optimization, i.e., our proposed version. 

Below shows how to evaluate different versions:

#### Option 1:

0\. Make sure you are under the ```pointnet2``` directory. <br>
1\. To run the **Baseline** version of PointNet++ (inference): <br>
```
python evaluate-baseline.py 
```

To check out all the optional arguments for the inference, please run: <br>
```
python evaluate-baseline.py -h
```

2\. To run the **Limited Delayed-Aggregation** version of PointNet++ (inference): <br>
```
python evaluate-limited.py
```

3\. To run the **Delayed-Aggregation** version of PointNet++ (inference): <br>
```
python evaluate.py 
```

4\. Check the results. It will print out the accuracy and latency after running: <br>
The Baseline version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87615576-06aa8080-c6e1-11ea-9a57-ab195c70ecef.jpg">

The Limited Delayed-Aggregation version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87615422-b3383280-c6e0-11ea-82a6-31be5e953cde.jpg">

The Delayed-Aggregation version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87615646-2cd02080-c6e1-11ea-881f-238d5d17e52a.jpg">

#### Option 2:
Switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there.

------------

### About
------------


