## DGCNN (Classification)

This repository contains code released for applying delayed-aggregation to [DGCNN](https://arxiv.org/abs/1801.07829) classification. <br>
The original implementation is [here](https://github.com/WangYueFt/dgcnn/tree/master).

For DGCNN (Segmentation), please check out the [part_seg](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn/part_seg) directory.


### Dataset
The classification task is tested on the [ModelNet40](https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip) (415M) dataset.
Use the following command to download the dataset if you skipped this step in `launcher.py`:
```
$ python download.py
```
If you want to experiment on other datasets, we suggest following the instructions [here](https://github.com/charlesq34/pointnet2#prepare-your-own-data) provided by the PointNet++ project.


### Environment/Libraries:
We highly recommend using virtual environment tools like Anaconda to set up an environment identical to the one we tested. <br>
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 3.7 <br>
Libraries: Tensorflow 1.15.0, numpy 1.18, cudnn 7.6.5, pillow 7.0.0

Compiler Toolchain:
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment.


---

### * Make sure to activate the correct environment before running any of the following commands.<br>

---



### Training
In this particular network, Limited Delayed-Aggregation is the same as the Fully Delayed-Aggregation because each module has only one MLP layer.
Below shows how to train different versions of DGCNN:

0\. Make sure you are under the ```dgcnn``` directory. <br>
1\. To train the **Baseline** version: <br>
```
$ python train-baseline.py
```

2\. To train the **Fully Delayed-Aggregation** version: <br>
```
$ python train.py
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python train.py -h
```

### Evaluation:
Below shows how to evaluate different versions of DGCNN:

0\. Make sure you are under the ```dgcnn``` directory. <br>
1\. To evaluate the **Baseline** version: <br>
```
$ python evaluate-baseline.py
```

2\. To evaluate the **Fully Delayed-Aggregation** version: <br>
```
$ python evaluate.py
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python evaluate.py -h
```

3\. Check the results. Below shows the example accuracy for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88492996-c5d22780-cf7c-11ea-9d65-e7eeb9fa340b.jpg"/>

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88493000-cff42600-cf7c-11ea-8f78-b28e0bba5ad7.jpg"/>


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
