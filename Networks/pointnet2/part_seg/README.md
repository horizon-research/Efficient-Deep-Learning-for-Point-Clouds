## PointNet++ (Segmentation)

This repository contains code released for applying delayed-aggregation to [PointNet++](https://arxiv.org/abs/1706.02413) segmentation. <br>
The original implementation is [here](https://github.com/charlesq34/pointnet2/tree/master/part_seg).

### Dataset
Pointnet++ object part segmentation uses the preprocessed <a href="https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip"> ShapeNetPart (674 MB)</a> dataset. <br>
Use the following command to download the dataset if you skipped this step in `launcher.py`:
```
$ python download.py
```

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
If you have done this step for the classification version, you can skip it now.<br>
Otherwise, please check out the instructions [here](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2#) for compilation.


### Training

Below shows how to train different versions of PointNet++:

0\. Make sure you are under the ```pointnet2/part_seg``` directory. <br>
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

0\. Make sure you are under the ```pointnet2/part_seg``` directory. <br>
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
<img src="https://user-images.githubusercontent.com/18485088/88263087-726b8b00-cc97-11ea-97ee-5f8b4ec312c8.jpg">

The **Limited Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88263117-81ead400-cc97-11ea-9747-dc6e7b358fc4.jpg">

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88263149-8e6f2c80-cc97-11ea-80f8-b26c915d1294.jpg">


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
