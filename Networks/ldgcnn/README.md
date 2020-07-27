## LDGCNN (Classification)

This repository contains code released for applying delayed-aggregation to [LDGCNN](https://arxiv.org/pdf/1904.10014.pdf) classification. <br>
The original implementation is [here](https://github.com/KuangenZhang/ldgcnn).



### Dataset
The classification task is tested on the [ModelNet40](https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip) (415M) dataset.
Use the following command to download the dataset if you skipped this step in `launcher.py`:
```
$ python download.py
```


### Environment/Libraries:
We highly recommend using virtual environment tools like Anaconda to set up an environment identical to the one we tested. <br>
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries: Tensorflow 1.12.0, numpy 1.14, CUDA 10.2, cudnn 7.6.5, scikit-learn

Compiler Toolchain:
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment.


---

### * Make sure to activate the correct environment before running any of the following commands.<br>

---


### Training
In this particular network, Limited Delayed-Aggregation is the same as the Fully Delayed-Aggregation because each module has only one MLP layer.
Below shows how to train different versions of LDGCNN:

0\. Make sure you are under the ```ldgcnn``` directory. <br>
1\. To train the **Baseline** version: <br>
```
$ python train.py --log_dir [MODEL_DIR] --model ldgcnn_baseline
```

2\. To train the **Fully Delayed-Aggregation** version: <br>
```
$ python train.py --log_dir [MODEL_DIR] --model ldgcnn
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python train.py -h
```

### Evaluation
Below shows how to evaluate different versions of LDGCNN:

0\. Make sure you are under the ```ldgcnn``` directory. <br>
1\. To evaluate the **Baseline** version: <br>
```
$ python evaluate.py --log_dir log_baseline --model_cnn ldgcnn_baseline
```

2\. To evaluate the **Fully Delayed-Aggregation** version: <br>
```
$ python evaluate.py --log_dir log_new --model_cnn ldgcnn
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python evaluate.py -h
```

The model for **Fully Delayed-Aggregation** version is stored in `models/ldgcnn.py`, and the model for **Baseline** version is stored in `models/ldgcnn_baseline.py`.

3\. Check the results. Below shows the example accuracy for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88492651-3f1c4b00-cf7a-11ea-83d6-6c8ba03451ea.jpg">


The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88492661-50fdee00-cf7a-11ea-8dc4-600fa757d428.jpg">


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
