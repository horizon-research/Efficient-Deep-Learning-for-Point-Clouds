## PointNet++ (Classification)

This repository contains code released for applying delayed-aggregation to [PointNet++](https://arxiv.org/abs/1706.02413) classification. <br>
The original implementation is [here](https://github.com/charlesq34/pointnet2).

For PointNet++ (Segmentation), please check out the [part_seg](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2/part_seg) directory.


### Dataset
The classification task is tested on the [ModelNet40](https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip) (415 MB) dataset.
Use the following command to download the dataset if you skip this step in `launcher.py`:
```
$ python download.py
```
If you want to experiment on other datasets, we suggest following the instructions [here](https://github.com/charlesq34/pointnet2#prepare-your-own-data) provided by the PointNet++ project.


### Environment/Libraries:
We highly recommend using virtual environment tools like Anaconda to set up an environment identical to the one we tested. <br>
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries: Tensorflow 1.12.0, numpy 1.14, CUDA 10.2, cudnn 7.6.5

Compiler Toolchain: 
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment.


---

### * Make sure to activate the correct environment before running any of the following commands.<br>

---

### Compile Customized Operators
Use the following command to compile the customized operators if you skipped this step in `launcher.py`:
```
$ python compile.py
```
If you encounter any compiling issues or you have multiple CUDA versions, modify the `compile.py` in `pointnet2` directory:

<img src="https://user-images.githubusercontent.com/18485088/88491154-00cd5e80-cf6f-11ea-85b7-257cb7ddb58f.jpg">

-	Modify the 3rd line `CUDA_PATH` to the one currently used by the system.
-	For futher information, we suggest following the original instructions [here](https://github.com/charlesq34/pointnet2#installation).


### Training

Below shows how to train different versions of PointNet++:

0\. Make sure you are under the ```pointnet2``` directory. <br>
1\. To train the **Baseline** version: <br>
```
$ python train-baseline.py
```

2\. To train the **Limited Delayed-Aggregation** version: <br>
```
$ python train-limited.py
```

3\. To train the **Fully Delayed-Aggregation** version: <br>
```
$ python train.py
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python train.py -h
```

### Evaluation
Below shows how to evaluate different versions of PointNet++:

0\. Make sure you are under the ```pointnet2``` directory. <br>
1\. To evaluate the **Baseline** version: <br>
```
$ python evaluate-baseline.py
```

2\. To evaluate the **Limited Delayed-Aggregation** version: <br>
```
$ python evaluate-limited.py
```

3\. To evaluate the **Fully Delayed-Aggregation** version: <br>
```
$ python evaluate.py
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python evaluate.py -h
```

4\. Check the results. Below shows the example accuracy for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88491548-763a2e80-cf71-11ea-9528-246c131a6914.jpg">

The **Limited Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88491561-91a53980-cf71-11ea-98dc-c0cdff0e7789.jpg">

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88491587-b699ac80-cf71-11ea-9429-56bbd7c17be5.jpg">


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
