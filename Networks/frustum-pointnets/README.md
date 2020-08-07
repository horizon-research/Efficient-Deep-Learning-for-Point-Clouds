## Frustum PointNets (3D Object Detection from RGB-D Data)

This repository contains code released for applying delayed-aggregation to [Frustum PointNets](https://arxiv.org/abs/1711.08488) 3D object detection. <br>
The original implementation is [here](https://github.com/charlesq34/frustum-pointnets).



### Dataset
The 3D object detection task is tested on the [KITTI](https://shapenet.cs.stanford.edu/media/frustum_data.zip) (960 MB) dataset.
Use the following command to download the dataset if you skipped this step in `launcher.py`:
```
$ python download.py
```
You can run `python train/provider.py` to visualize the training data (frustum point clouds and 3D bounding box labels, in rect camera coordinate).


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
Install <a href="https://www.tensorflow.org/install/">TensorFlow</a>.There are also some dependencies for a few Python libraries for data processing and visualizations like `cv2`, `mayavi`  etc. It's highly recommended that you have access to GPUs.

Suppose the root directory is at `frustum-pointnets`. Compile several custom Tensorflow operators from PointNet++. The TF operators are included under `models/tf_ops`, you need to compile them (check `tf_xxx_compile.sh` under each ops subfolder) first. Update `cuda` and `python` path if necessary. Assuming the paths are all correct. you can use the script `compile.py` to compile those modules.
```
$ python compile.py
```
Then, compile the evaluation code in `train/kitti_eval`, go to the directory `train/kitti_eval` and run:
```
$ ./compile.sh
```
Check `train/kitti_eval/README.md` for details.


### Training

Below shows how to train different versions of Frustum PointNets:

0\. Make sure you are under the ```frustum-pointnets``` directory. <br>
1\. To train the **Baseline** version: <br>
```
$ bash scripts/command_train_v2_baseline.sh
```

2\. To train the **Limited Delayed-Aggregation** version: <br>
```
$ bash scripts/command_train_v2_limited.sh
```

3\. To train the **Fully Delayed-Aggregation** version: <br>
```
$ bash scripts/command_train_v2.sh
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python train/train.py -h
```

### Evaluation
Below shows how to evaluate different versions of Frustum PointNets:

0\. Make sure you are under the ```frustum-pointnets``` directory. <br>
1\. To evaluate the **Baseline** version: <br>
```
$ bash scripts/command_test_v2_baseline.sh
```

2\. To evaluate the **Limited Delayed-Aggregation** version: <br>
```
$ bash scripts/command_test_v2_limited.sh
```

3\. To evaluate the **Fully Delayed-Aggregation** version: <br>
```
$ bash scripts/command_test_v2.sh
```

Add ``` -h``` after the above commands to check out all the optional arguments, e.g.: <br>
```
$ python train/test.py -h
```

**NOTE**: In our paper, we report the accuracy from the `Eval` set. Here we show the sample accuracy of Brid Eye View (BEV) accuracy.

4\. Check the results. Below shows the example accuracy for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88494248-3714d900-cf83-11ea-89d8-503cdd290202.png">

The **Limited Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88494269-53b11100-cf83-11ea-80d3-6d89ef7f03e3.png">

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88494281-6592b400-cf83-11ea-8284-4632e9225c91.png">


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
