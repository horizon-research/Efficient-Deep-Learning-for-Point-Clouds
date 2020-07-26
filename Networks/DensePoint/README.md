### DensePoint (Classification)
------------
This repository is the code release for applying the delayed-aggregation method on DensePoint. The DensePoint paper reference can be found [here](https://arxiv.org/pdf/1909.03669.pdf). 
For more detailed information about original implementation, please visit the GitHub repository [here](https://github.com/Yochengliu/DensePoint).


### Dataset
The classification task is tested on the [ModelNet40](https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip) (415M) benchmark.
Use the following command to download the dataset if you skipped this step in launcher.py:
```
$ python download.py
```


### Environment/Libraries:
We highly recommend using virtual environment tools like Anaconda to set up an environment identical to the one we tested. <br>
We have been experimenting in the environment below:

OS: Ubuntu 16.04.6 LTS <br>
Python: 3.5 <br>
Libraries: Pytorch 0.3.0, numpy 1.13, CUDA 8.0, cudnn 5.1.10

Compiler Toolchain:
- gcc / gxx: 5.5.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment.


### Creating Environment
We use the following instructions to create and manage the working environment in Anaconda3. Steps with ***** are optional.

*Add channels to support earlier versions of dependencies if necessary. 
```
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```
Create Conda environment.
```
$ conda create -n DensePoint python=3.5
```
*Isolate the Conda environment from global/user site-packages.
```
$ export PYTHONNOUSERSITE=1
```
Activate Conda environment.
```
$ conda activate DensePoint
```
Install PyTorch 0.3.0 and CUDA 8.0.
```
$ conda install pytorch=0.3.0 cuda80 -c pytorch
```
Install cuDNN 5.1.
```
$ conda install cudnn=5.1
```
Install other dependencies.
```
$ conda install torchvision h5py pyyaml scipy
```

### Compile Customized Operators
Use the following command to compile the customized operators if you skipped this step in launcher.py:
```
$ python compile.py
```
If you encounter any compiling issues or you have multiple CUDA versions, modify the `CMakeList.txt`:

-    Comment out 4th line: **find_package(CUDA REQUIRED)**.
-    Uncomment 6th and 7th line: **set(CUDA_TOOLKIT_ROOT_DIR)** and **find_package(CUDA)**, and then change the CUDA version to the one currently used by the system.


### Training
In this particular network, Limited Delayed-Aggregation is the same as the full Delayed-Aggregation because each module has only one MLP layer.
Below shows how to train different versions of DensePoint:

0\. Make sure you are under the ```DensePoint``` directory. <br>
1\. To train the **Baseline** version: <br>
```
$ bash train-baseline.sh
```

2\. To train the **Fully Delayed-Aggregation** version: <br>
```
$ bash train.sh
```

Modify the `$checkpoint$` to `' '`in `cfgs/config_cls.yaml` if you want to start the training from scratch. Otherwise, it will continue from the saved model.


### Evaluation
Below shows how to evaluate different versions of DensePoint:

0\. Make sure you are under the ```DensePoint``` directory. <br>
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

**Note that model_cls_L6_iter_36567_acc_0.923825_ori_bkup.pth is the pre-trained model provided by the original DensePoint repo.*

3\. Check the results. Below shows the example accuracies and latency for different versions: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88476732-ca5cf880-cf08-11ea-92bf-d3fc8c02898f.jpg">

The **Fully Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/18485088/88476739-d8ab1480-cf08-11ea-92fd-d2e4fa97df21.jpg">


***You can also switch back to [the root directory](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) and follow the instructions there for training and evaluation.***
