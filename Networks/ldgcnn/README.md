### LDGCNN (Classification)
------------
This repository is code released for applying delayed-aggregation to [LDGCNN](https://arxiv.org/pdf/1904.10014.pdf). the original implementation is [here](https://github.com/KuangenZhang/ldgcnn). 

---

### Dataset 
Currently, we tested our model on ModelNet40 benchmark. To download the dataset, run: 
```
python download_modelnet.py
``` 

---

### Environment/Libraries: 
We tested our implementation in the environment below:
-   Ubuntu 18.04.3 LTS
-   Python: 2.7 <br>
- gcc / gxx: 7.3.0 (to compile the tf ops)
-   Dependencies: Tensorflow 1.12.0, numpy 1.14, scikit-learn, CUDA 10.2, cudnn 7.6.5

---

### Evaluation

There are two different versions of LDGCNN: <br>
**Baseline**: the original LDGCNN network with implementation optimizations. <br>
**Delayed-Aggregation**: the version with full delayed-aggregation optimization, i.e., our proposed version. <br>

(In this special case, this Limited Delayed-Aggregation version is the same as the Delayed-Aggregation version.

0\. Make sure you are at the `ldgcnn` directory. <br>
1\. To run the **Baseline version** of LDGCNN (inference):
```
python evaluate.py --log_dir log_baseline --model_cnn ldgcnn_baseline
```

2\. To run our **Delayed-Aggregation version** of LDGCNN (inference):
```
python evaluate.py --log_dir log_new --model_cnn ldgcnn
```

3\. To check out both model archtectures, our **Delayed-Aggregation version** is stored in `models/ldgcnn.py` and the **Baseline version** is stored in `models/ldgcnn_baseline.py`.

