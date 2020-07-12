### LDGCNN (Classification)
------------
This repository is code released for applying delayed-aggregation to [LDGCNN](https://arxiv.org/pdf/1904.10014.pdf). the original implementation is [here](https://github.com/KuangenZhang/ldgcnn). 

### 1. Dataset 
Currently, we tested our model on ModelNet40 benchmark. To download the dataset, run: 
```
python download_modelnet.py
``` 
### 2. Environment/Libraries: 
We tested our implementation in the environment below:
-   Ubuntu 18.04.3 LTS
-   Python: 2.7 <br>
- gcc / gxx: 7.3.0 (to compile the tf ops)
-   Dependencies: Tensorflow 1.12.0, numpy 1.14, CUDA 10.2, cudnn 7.6.5

### 3. Run LDGCNN Model

This section is about how to run (inferences on) the two different versions of LDGCNN below: <br>
**Baseline**: the original implementation of the LDGCNN. <br>
**Delayed-Aggregation**: the one with full delayed-aggregation optimization, i.e., our proposed version. <br>

(In this special case, this Limited Delayed-Aggregation version is the same as the Delayed-Aggregation version._

0\. To run both the original network and the optimized network, go to `ldgcnn` directory.
1\. To run the **Baseline version** of LDGCNN (inference):
```
python evaluate.py --log_dir log_baseline --model_cnn ldgcnn_baseline
```

2\. To run our **Delayed-Aggregation version** of LDGCNN (inference):
```
python evaluate.py --log_dir log_new --model_cnn ldgcnn
```

3\. To check out both model archtectures, our **Delayed-Aggregation version** is stored in `models/ldgcnn.py` and the **Baseline version** is stored in `models/ldgcnn_baseline.py`.

