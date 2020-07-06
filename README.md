## Efficient Deep Learning for Point Clouds
This project is about designing efficient 3-d point cloud Deep Neural Networks with pure algorithm (software-level) optimizations. We propose a technique named **Delayed Aggregation** that:
1. reduces redundant computation to achieve workload efficiency; 
2. exposes parallelism that can be easily captured by the underlying hardware.

We first provide some background on Point Cloud NNs, and introduce how **Delayed Aggregation** works: 

### Background on Point Cloud NNs
In most Point Cloud neural networks, there are three major operations: **Neighbor Search**, **Aggregation**, and **Feature Computation**.
Take the first layer of [PointNet++](https://github.com/charlesq34/pointnet2) as an example: 
![image](https://user-images.githubusercontent.com/19209239/86542069-20c5b100-bee0-11ea-9f63-5eb19cdaf63c.png)

**Neighbor Search** computes the neighbor information for each point, and generates a *Neighbor Index Table*. 

**Aggregation** gathers select neighborhoods the using the *Neighbor Index Table*. (Is simply takes in point indices, accesses the memory, and returns the accessed data). Each neighborhood consists of the central point's and all its neighbors' feature vectors. In this example, the Aggregation generates a 512 x 32 x 3 tensor (512: number of neighborhoods; 32: number of neighbors in each neighborhood; 3: dimension of feature vectors). 

**Feature Computation** consists of multiple MLPs. 

At the end of the layer, there is usually a reduction operation. (In this example, it is a Max opeation). It is worth noting that this reducation operation is sometimes referred to as an aggregation operation. This operation is not what we mean by Aggregation. The reduction is trivial from a compute perspective: the three steps above take nearly 100% of the execution time. 

In most networks, e.g., [PointNet++](https://github.com/charlesq34/pointnet2) and [DGCNN](https://github.com/WangYueFt/dgcnn), the three steps are done in order sequentially.

### How does Delayed Aggregation work

**Delayed Aggregation** does the Feature Computation first and does Aggregation after the entire Feature Computation is done. Meanwhile, Neighbor Search is done in parallel with Feature Computation. It is a form of approximation, but our experimental results indicate the accuracy does not drop (with fine-tuning). 
- Why do we delay Aggregation? </br>
It not only reduces the overall compute workload, but also introduces parallelism into the pipeline (now Neighbor Search can be done in parallel with MLPs). 

- What is changed from the algorithm's perspective?</br> 
Now the Feature Computation step computes the feature of individual points instead of neighborhoods.

Below is how the first layer of PointNet++ looks like with Delayed Aggregation: 
![image](https://user-images.githubusercontent.com/19209239/86542082-32a75400-bee0-11ea-82ce-dacac1fc8812.png) 

**Limited Delayed Aggregation**
- [ ] to-do
------------------

### Networks
Delayed-aggregation applies to a wide range of different point cloud networks. This repo has the implementation for the following five networks:

- PointNet++: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/pointnet2), Segmentation - Optimized Version
- DGCNN: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn), [Segmentation - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/dgcnn/part_seg)
- LDGCNN: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/ldgcnn)
- F-PointNet: [3D Detection](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/frustum-pointnets)
- DensePoint: [Classification - Optimized Version](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/DensePoint)

Also, for a comprehensive evaluation, we have provided three versions of each network: 
1. **Baseline**: the original implementation of the networks.
2. **Limited Delayed-Aggregation**: the one with limited delayed-ggregation optimization, which is inspired by some GNNs implementations.
3. **Fully Delayed-Aggregation**: the one with full delayed-aggregation optimization, i.e., our proposed technique.

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
Current Python script works for all the networks, except `DensePoint`. To run `DensePoint`, please check out the [sub-repository](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds/tree/master/Networks/DensePoint) for details.

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
