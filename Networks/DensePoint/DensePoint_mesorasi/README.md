### DensePoint (Classification)
------------
This repository is the code release for applying the delayed-aggregation method on DensePoint. The DensePoint paper reference can be found [here](https://arxiv.org/pdf/1909.03669.pdf). 
For more detailed information, please visit the GitHub repository [here](https://github.com/Yochengliu/DensePoint). 

### Prerequisite
We tested our implementation on the environment listed below:
-   Ubuntu 16.04.6 LTS
-   Python: 3.5 <br>
-     gcc / gxx: 5.5.0 (to compile the tf ops)
-   Dependencies:
    - Pytorch 0.3.0 
    - numpy 1.13
    - CUDA 8.0
    - cuDNN 5.1.10
    
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

### Preparing Dataset 
The classification task is tested on the [ModelNet40](https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip) (415M) benchmark. To download the dataset, change the directory to `Dataset` and run: 
```
$ wget https://shapenet.cs.stanford.edu/media                /modelnet40_ply_hdf5_2048.zip
``` 
Unzip the dataset and change the `$data_root$` in `cfgs/config_cls.yaml`.

### Building Kernel
Change directory to `Networks/DenseNet/` and create `build` folder.
```
$ mkdir build && cd build
```
Modify the `CMakeList.txt` if there are multiple CUDA versions.

-    Comment out 4th line: **find_package(CUDA REQUIRED)**.
-    Uncomment 6th and 7th line: **set(CUDA_TOOLKIT_ROOT_DIR)** and **find_package(CUDA)**, and then change the CUDA version to the one currently used by the system.

Build the kernel.
```
$ cmake .. && make
```

### Run DensePoint Model
Our efficient version (`DensePoint_mesorasi`) of DensePoint shares the identical directory structure with the baseline version (`DensePoint_baseline`). We provide the pre-trained models in `cls` and the training logs in `log_example` for both versions.

To run the inference on both the baseline version and our optimized version, change the directory to the corresponding folder and run:
```
$ python voting_evaluate_cls.py
```

Training on both versions can be executed by:
```
$ ./train_cls.sh
```
Modify the `$checkpoint$` to `' '`in `cfgs/config_cls.yaml` if one wants to start the training from scratch. Otherwise, it will continue from the saved model.

**Note that model_cls_L6_iter_36567_acc_0.923825_ori_bkup.pth is the pre-trained model provided by the original DensePoint repo.*

### License

The code is released under MIT License (see LICENSE file for details).

### Acknowledgement

The code is heavily borrowed from [Pointnet2_PyTorch](https://github.com/erikwijmans/Pointnet2_PyTorch).

