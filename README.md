## Efficient-Deep-Learning-for-Point-Clouds
This project is about designing efficient 3-d point cloud Deep Neural Networks with pure algorithm (software-level) optimizations. Our techniques: 
1. reduce redundant computation to achieve workload efficiency; 
2. expose parallelism that can be easily captured by the underlying hardware.

------------------

### Optimized Networks
We have applied the optimizations to the networks below:

- PointNet++: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2), Segmentation - Optimized Version
- DGCNN: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn), [Segmentation - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn/part_seg)
- LDGCNN: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/ldgcnn)
- F-PointNet: [3D Detection](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/frustum-pointnets)
- DensePoint [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/DensePoint)

### How to Run Networks
We have create a simple PYTHON script to navigate the repository. Run:
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
                        network, use: --compile [NETWORK_NAME] or to copmpile
                        all models using, --compile all
  --download DOWNLOAD   Download the specific dataset for the models, to
                        download a dataset for a specific network, use:
                        --compile [NETWORK_NAME] or to copmpile all models
                        using, --compile all
  --list_models LIST_MODELS
                        List all model names.
  --run RUN             Launch the model with default settings.
  --train TRAIN         Train the model with default settings.
  --use_baseline USE_BASELINE
                        Use baseline instead of efficient version.
  --use_limited USE_LIMITED
                        Use limited aggr. instead of efficient version.
```
Current PYTHON script works for most of networks,except for `DensePoint`. To compile and run `DensePoint`, please check out the [sub-repository](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/DensePoint) for details.  For most of networks, you don't have to compile any additional modules, most of them are native PYTHON code. But for `pointnet++` and `f-pointnet`, we need to compile some modules. To compile, you can run:
```
$ python launcher.py --compile [NETWORK]
```
`[NETWORK]` can be `pointnet2` (for `pointnet++`) or `frustum-pointnets` (for `f-pointnet`), or simply compile all by using `all`.

After the compilation, you need to download the dataset for the networks. To do so, by using:
```
$ python launcher.py --download [NETWORK]
```

Now, if everything goes well, you can run our models by using:
```
$ python launcher.py --run [NETWORK]
```
To run the corresponding baseline, you can use additional flag `--use_baseline`:
```
$ python launcher.py --run [NETWORK] --use_baseline
```
To run the corresponding limited aggregated version, you can use additional flag `--use_limited`:
```
$ python launcher.py --run [NETWORK] --use_limited
```


### Acknowledgement ###
------------------
