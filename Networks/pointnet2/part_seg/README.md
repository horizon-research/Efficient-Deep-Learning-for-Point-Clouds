### PointNet++ (Segmentation)
------------

### To-do
- [ ] add limited version
- [ ] update training script
- [ ] retrain model with most updated version
- [ ] update README

### Prerequisite
### 1. Dataset
Please follow instructions given by the original [PointNet++](https://github.com/charlesq34/pointnet2/blob/master/README.md#object-part-segmentation) project: <br>Preprocessed ShapeNetPart dataset (XYZ, normal and part labels) can be found <a href="https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip">here (674MB)</a>. Move the uncompressed data folder to `data/shapenetcore_partanno_segmentation_benchmark_v0_normal`

### 2. Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 2.7 <br>
Libraries:
- Tensorflow 1.12.0 
- numpy 1.14
- CUDA 10.2
- cudnn 7.6.5

Compiler Toolchain: 
- gcc / gxx: 7.3.0 (to compile the tf ops)

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### 3. Compile:
If you have done the compile step for classification, there is no need to do so again.

This part is to compile the [customized tf operators](https://github.com/charlesq34/pointnet2#compile-customized-tf-operators) (interpolation, grouping, sampling). Please follow the steps below.<br>
0\. Suppose we are in the ```pointnet2``` directory: <br>
<img src="https://user-images.githubusercontent.com/19209239/83693739-a7772d80-a5c4-11ea-8459-f0e6841f29e8.png" alt="drawing" width="600"/>

1\. Enter directory ```./tf_ops/3d_interpolation``` and check if the CUDA path in the ```tf_interpolate_compile.sh``` script is set correctly; if not, please correct: <br>
<img src="https://user-images.githubusercontent.com/19209239/83694347-d8a42d80-a5c5-11ea-850c-261019637fa2.png" alt="drawing" width="1000"/>

2\. Run ```sh tf_interpolate_compile.sh```.<br>
3\. Repeat 1-2 for ```./tf_ops/grouping``` and ```./tf_ops/sampling```. <br><br>
Or, if the CUDA paths are already set correctly, run 
```python compile.py``` in the ```pointnet2``` directory. 

### 4. Run:
This part is to run the inference on both the original network and the optimized network. <br><br>
0\. Make sure you are at the ```pointnet2/part_seg``` directory. <br>
1\. To run the **original version** of PointNet++ (evaluation / inference): <br>
```
python evaluate-baseline.py 
```

To check out all the optional arguments for the inference, please run: <br>
```
python evaluate-baseline.py -h
```

2\. To run the **optimized version** of PointNet++ (evaluation / inference): <br>
```
python evaluate.py 
```

To check out all the optional arguments for the inference, please run: <br>
```
python evaluate.py -h
```

3\. Check the results. After running as in step 1 and 2.

------------

### About
------------
