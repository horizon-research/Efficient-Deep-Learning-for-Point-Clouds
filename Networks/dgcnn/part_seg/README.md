## DGCNN (Segmentation)

This repository contains code released for applying delayed-aggregation to [DGCNN](https://arxiv.org/abs/1801.07829) segmentation. <br>
The original implementation is [here](https://github.com/WangYueFt/dgcnn/tree/c8fd0cd2a2d47747cb3a137c28e7346b69284d45/tensorflow/part_seg).

### Dataset
DGCNN object part segmentation uses the original <a href="https://shapenet.cs.stanford.edu/ericyi/shapenetcore_partanno_v0.zip"> ShapeNetPart (1.0 GB)</a> and <a href="https://shapenet.cs.stanford.edu/media/shapenet_part_seg_hdf5_data.zip"> HDF5 (346 MB)</a> dataset. <br>
Use the following command to download the dataset if you skipped this step in `launcher.py`:
```
$ python download.py
```

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



### Training:
In this particular network, Limited Delayed-Aggregation is the same as the Fully Delayed-Aggregation because each module has only one MLP layer.
Below shows how to train different versions of DGCNN:

0\. Make sure you are under the ```dgcnn/part_seg``` directory. <br>
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

### Evaluation
Below shows how to evaluate different versions of DGCNN:

0\. Make sure you are under the ```dgcnn/part_seg``` directory. <br>
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

4\. Check the results. Below shows the example accuracy for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/19209239/83949089-e63cfb80-a7ef-11ea-87ee-89f50b5a9c06.png" alt="drawing" width="520"/>

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/19209239/83948972-1cc64680-a7ef-11ea-92dd-344788e006b1.png" alt="drawing" width="520"/>


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
