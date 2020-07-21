## PointNet++ (Classification)

For PointNet++ (Segmentation), please check out the [part_seg](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2/part_seg) directory.


### Dataset
Currently, we only support the ModelNet benchmark used by the [original PointNet++ project](https://github.com/charlesq34/pointnet2). To download the dataset, run: 
```
python modelnet_h5_dataset.py
``` 
If you want to experiment on your own dataset, we suggest following the instructions [here](https://github.com/charlesq34/pointnet2#prepare-your-own-data).


### Environment/Libraries:
We highly recommend using virtual environment tools like Anaconda to set up an environment identical to the one we tested. <br>
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries: Tensorflow 1.12.0, numpy 1.14, CUDA 10.2, cudnn 7.6.5

Compiler Toolchain: 
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 


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

### Training

Below shows how to train different versions of PointNet++:

0\. Make sure you are under the ```pointnet2``` directory. <br>
1\. To train the **Baseline** version: <br>
```
python train-baseline.py 
```

2\. To train the **Limited Delayed-Aggregation** version: <br>
```
python train-limited.py
```

3\. To train the **Fully Delayed-Aggregation** version: <br>
```
python train.py 
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
python train.py -h
```

### Evaluation
Below shows how to evaluate different versions of PointNet++:

#### Option 1: 

0\. Make sure you are under the ```pointnet2``` directory. <br>
1\. To evaluate the **Baseline** version: <br>
```
python evaluate-baseline.py 
```

2\. To evaluate the **Limited Delayed-Aggregation** version: <br>
```
python evaluate-limited.py
```

3\. To evaluate the **Fully Delayed-Aggregation** version: <br>
```
python evaluate.py 
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
python evaluate.py -h
```

5\. Check the results. Below shows the example accuracies and latency for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87615576-06aa8080-c6e1-11ea-9a57-ab195c70ecef.jpg">

The **Limited Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87957882-d830fa80-ca7e-11ea-9263-0d9d728b287e.jpg">

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/87615646-2cd02080-c6e1-11ea-881f-238d5d17e52a.jpg">

#### Option 2:
Switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there.


