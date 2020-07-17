## DGCNN (Segmentation)

### Dataset
Currently, we only support the ShapeNet benchmark used by the [original DGCNN project](https://github.com/WangYueFt/dgcnn/tree/master/tensorflow/part_seg). To download the dataset, please run: <br>
```
sh +x download_data.sh
```

then run: <br>
```
unzip shapenetcore_partanno_v0.zip
```

### Environment/Libraries:
This is a tricky part. It is necessary to install the right versions of libraries to get the code running.
We have been experimenting in the environment below:

OS: Ubuntu 18.04.3 LTS <br>
Python: 3.7 <br>
Libraries: Tensorflow 1.15.0, numpy 1.18, cudnn 7.6.5, pillow 7.0.0

We highly recommend using virtual environment tools like Anaconda to set up the right environment. 

### Training:
In this particular network, Limited Delayed-Aggregation is the same as the full Delayed-Aggregation because each module has only one MLP layer. <br>
0\. Make sure you are at the ```dgcnn/part_seg``` directory. <br> 
1\. To train the **Baseline version** of DGCNN (seg): <br>
``` 
python train_baseline.py
```

2\. To train the **Delayed-Aggregation version** of DGCNN (seg): <br>
``` 
python train.py
```

### Evaluation:

0\. Make sure you are at the ```dgcnn/part_seg``` directory. <br>
1\. To run the **Baseline version** of DGCNN (inference): <br>
```
python test_baseline.py 
```

2\. To run the **Delayed-Aggregation version** of DGCNN (inference): <br>
```
python test.py 
```

3\. Check the results. After running, it will print out the accuracy and latency: <br>
The **Baseline** version: <br>
<img src="https://user-images.githubusercontent.com/19209239/83949089-e63cfb80-a7ef-11ea-87ee-89f50b5a9c06.png" alt="drawing" width="520"/>

The **Delayed-Aggregation** version: <br>
<img src="https://user-images.githubusercontent.com/19209239/83948972-1cc64680-a7ef-11ea-92dd-344788e006b1.png" alt="drawing" width="520"/>

