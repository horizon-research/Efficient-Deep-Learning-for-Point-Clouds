## Efficient Deep Learning for Point Clouds
This project is about designing efficient point cloud Deep Neural Networks with pure algorithm (software-level) optimizations. We propose a technique named **Delayed-Aggregation**, which:
1. reduces redundant computation to achieve workload efficiency; 
2. exposes parallelism that can be easily captured by the underlying hardware.

For the background of point cloud neural networks and how our delayed-aggregation helps improves the execution efficiency, see the [wiki](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/wiki) page.


### Networks
Delayed-aggregation applies to a wide range of different point cloud networks. This repo has the implementation for the following five networks:

- PointNet++: [Classification](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2), [Segmentation](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2/part_seg)
- DGCNN: [Classification](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn), [Segmentation](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn/part_seg)
- LDGCNN: [Classification](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/ldgcnn)
- F-PointNet: [3D Detection](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/frustum-pointnets)
- DensePoint: [Classification](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/DensePoint)

For each network, we have provided three versions:
1. **Baseline**: the original networks with implementation optimizations.
2. **Limited Delayed-Aggregation**: the one with limited delayed-aggregation optimization, which is inspired by some GNNs implementations.
3. **Fully Delayed-Aggregation**: the one with full delayed-aggregation optimization, i.e., our proposed technique.

For the difference between the three versions, again see the [wiki](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/wiki) page.


### How to Run
We have created a simple PYTHON script to navigate the repository. Run:
```
$ python launcher.py -h
```
You will see:
```
usage: launcher.py [-h] [--compile COMPILE] [--download DOWNLOAD]
                   [--list_models LIST_MODELS] [--run RUN] [--train TRAIN]
                   [--use_baseline USE_BASELINE] [--use_limited USE_LIMITED]
                   [--segmentation SEGMENTATION]

optional arguments:
  -h, --help            show this help message and exit
  --compile COMPILE     Compile libraries in the models, to compile a specific
                        network, use: --compile [NETWORK_NAME] or to compile
                        all models using, --compile all
  --download DOWNLOAD   Download the specific dataset for the models, to
                        download a dataset for a specific network, use:
                        --download [NETWORK_NAME] or to download all datasets
                        using, --download all
  --list_models LIST_MODELS
                        List all model names.
  --run RUN             Evaluate the model with Fully Delayed-Aggregation.
  --train TRAIN         Train the model with Fully Delayed-Aggregation.
  --use_baseline USE_BASELINE
                        Use the baseline without any kind of Delayed-Aggregation.
  --use_limited USE_LIMITED
                        Use Limited Delayed-Aggregation.
  --segmentation SEGMENTATION
                        Execute the segmentation version.
```

There is a slight naming difference between the actual model name and the name in the code. Make sure you use names in the second column of this table to run the `launcher.py`. 

| Actual Model Name | Name in Our Code |
|-------------------|------------------|
| PointNet++        | pointnet2        |
| DGCNN             | dgcnn            |
| LDGCNN            | ldgcnn           |
| F-PointNet        | frustum-pointnets|
| DensePoint        | DensePoint       | 


### Dataset
Datasets shared by multiple networks are placed in the `Datasets` directory, e.g., ModelNet40 and ShapeNet.<br>
Datasets exclusively used by a network are placed in its directory, e.g., `KITTI` for `F-PointNet`.<br>
Use the following command to download dataset:
```
$ python launcher.py --download [NETWORK]
```
- Specify [NETWORK] to the name of a network to download the corresponding dataset or `all` to download all the datasets.
- Add `--segmentation True` to download segmentation data for `pointnet++` and `dgcnn`.

---

### * Make sure to activate the correct environment for each network before running any of the following commands.<br>

---

### Compile Customized Operators
Some networks are native Python code and do not need to compile. Others such as `pointnet++`, `f-pointnet`, and `DensePoint` have customized modules that need to be compiled.<br>
To compile, run:
```
$ python launcher.py --compile [NETWORK]
```
- `[NETWORK]` can be `pointnet2` (for `pointnet++`), `frustum-pointnets` (for `f-pointnet`), `DensePoint` (for `DensePoint`), or simply compile all by using `all`.
- Please check out the instructions in each network to modify the `CUDA_PATH` if you encounter any compiling issues.


### Training
To train the Baseline version, add flag `--use_baseline True`:
```
$ python launcher.py --train [NETWORK] --use_baseline True
```
To train the Limited Delayed-Aggregation version, add flag `--use_limited True`:
```
$ python launcher.py --train [NETWORK] --use_limited True
```
To train the Fully Delayed-Aggregation version:
```
$ python launcher.py --train [NETWORK]
```
To train the segmentation model of `pointnet++` and `dgcnn`, add flag `--segmentation True` to the above commands:
```
$ python launcher.py --train [NETWORK] --segmentation True
```


### Evaluation
To evaluate the Baseline version, add flag `--use_baseline True`:
```
$ python launcher.py --run [NETWORK] --use_baseline True
```
To evaluate the Limited Delayed-Aggregation version, add flag `--use_limited True`:
```
$ python launcher.py --run [NETWORK] --use_limited True
```
To evaluate the Fully Delayed-Aggregation version:
```
$ python launcher.py --run [NETWORK]
```
To evaluate the segmentation model of `pointnet++` and `dgcnn`, add flag `--segmentation True` to the above commands:
```
$ python launcher.py --run [NETWORK] --segmentation True
```


### Publication ###
This project contains the artifact for our paper [Mesorasi: Architecture Support for Point Cloud Analytics via Delayed-Aggregation](https://www.cs.rochester.edu/horizon/pubs/micro20-mesorasi.pdf) (MICRO 2020).

```
@inproceedings{feng2020mesorasi,
  title={Mesorasi: Architecture Support for Point Cloud Analytics via Delayed-Aggregation},
  author={Feng, Yu and Tian, Boyuan and Xu, Tiancheng and Whatmough, Paul and Zhu, Yuhao},
  booktitle={Proceedings of the 53th International Symposium on Microarchitecture},
  year={2020},
  organization={ACM}
}
```
