## Efficient Deep Learning for Point Clouds
This project is about designing efficient 3-d point cloud Deep Neural Networks with pure algorithm (software-level) optimizations. We propose a technique named **Delayed Aggregation** that:
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

For each network, we have provided three versions of each network: 
1. **Baseline**: the original networks with implementation optimizations.
2. **Limited Delayed-Aggregation**: the one with limited delayed-aggregation optimization, which is inspired by some GNNs implementations.
3. **Fully Delayed-Aggregation**: the one with full delayed-aggregation optimization, i.e., our proposed technique.

For the difference between the three versions, again see the [wiki](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/wiki) page.

### How to Run Networks
We have created a simple PYTHON script to navigate the repository. Run:
```
$ python launcher.py -h
```
You will see:
```                    
usage: launcher.py [-h] [--compile COMPILE] [--download DOWNLOAD]
                   [--list_models LIST_MODELS] [--run RUN] [--train TRAIN]
                   [--use_baseline USE_BASELINE] [--use_limited USE_LIMITED]

optional arguments:
  -h, --help            show this help message and exit
  --compile COMPILE     Compile libraries in the models, to compile a specific
                        network, use: --compile [NETWORK_NAME] or to compile
                        all models using, --compile all
  --download DOWNLOAD   Download the specific dataset for the models, to
                        download a dataset for a specific network, use:
                        --compile [NETWORK_NAME] or to compile all models
                        using, --compile all
  --list_models LIST_MODELS
                        List all model names.
  --run RUN             Launch the model with default settings.
  --train TRAIN         Train the model with default settings.
  --use_baseline USE_BASELINE
                        Use baseline instead of the efficient version.
  --use_limited USE_LIMITED
                        Use limited aggregation instead of the efficient version.
```

There is a slight naming difference between the actual model name and the name in the code. Make sure you use names in the second column of this table to run the `launcher.py`. 

| Actual Model Name | Name in Our Code |
|-------------------|------------------|
| PointNet++        | pointnet2        |
| DGCNN             | dgcnn            |
| LDGCNN            | ldgcnn           |
| F-PointNet        | frustum-pointnets|
| DensePoint        | DensePoint       | 

For most of the networks, you don't have to compile any additional modules, most of them are native Python code. But for `pointnet++` and `f-pointnet`, you need to compile some modules. To compile, you can run:
```
$ python launcher.py --compile [NETWORK]
```
`[NETWORK]` can be `pointnet2` (for `pointnet++`) or `frustum-pointnets` (for `f-pointnet`), or simply compile all by using `all`.

After the compilation, you need to download the dataset for the networks. To do so, by using:
```
$ python launcher.py --download [NETWORK]
```

Now, if everything goes well, you can run the full delayed-aggregation version of the models by:
```
$ python launcher.py --run [NETWORK]
```
To run the baseline, you can use additional flag `--use_baseline`:
```
$ python launcher.py --run [NETWORK] --use_baseline
```
To run the models with the limited delayed-aggregation, you can use additional flag `--use_limited`:
```
$ python launcher.py --run [NETWORK] --use_limited
```


### Publication ###
------------------
This project contains the artifact for our paper [Mesorasi: Enabling Efficient Point Cloud Analytics via Delayed-Aggregation]() (MICRO 2020).

```
@inproceedings{feng2020mesorasi,
  title={Mesorasi: Enabling Efficient Point Cloud Analytics via Delayed-Aggregation},
  author={Feng, Yu and Xu, Tiancheng and Tian, Boyuan and Whatmough, Paul and Zhu, Yuhao},
  booktitle={Proceedings of the 53th International Symposium on Microarchitecture},
  year={2020},
  organization={ACM}
}
```

