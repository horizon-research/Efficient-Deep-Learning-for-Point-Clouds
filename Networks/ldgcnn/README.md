### LDGCNN (Classification)
------------
This repository is code release for applying delayed-aggregation method on LDGCNN. The LDGCNN paper reference can be found in [here](https://arxiv.org/pdf/1904.10014.pdf). 
For more detailed information please visit the github repository [here](https://github.com/KuangenZhang/ldgcnn). 

### Prerequisite
We tested our implementation on the environment listed below:
-   Ubuntu 18.04.3 LTS
-   Python: 2.7 <br>
- gcc / gxx: 7.3.0 (to compile the tf ops)
-   Dependencies:
    - Tensorflow 1.12.0 
    - numpy 1.14
    - CUDA 10.2
    - cudnn 7.6.5

### Preparing Dataset 
Currently, we tested our model on ModelNet40 benchmark. To download the dataset, run: 
```
python download_modelnet.py
``` 

### Run LDGCNN Model

We upload the pre-trained models of both our efficient version and original model to this repo. Our efficient version is stored in `log_new` directory and original version is stored in `log_baseline` directory. 

To run the inference on both the original network and the optimized network, go to `ldgcnn` directory.

To run the **original version** of ldgcnn inference:
```
python evaluate.py --log_dir log_baseline --model_cnn ldgcnn_baseline
```
To run our **efficient version** of ldgcnn inference:
```
python evaluate.py --log_dir log_new --model_cnn ldgcnn
```

To check out both model archtectures, our **efficient version** is stored in `models/ldgcnn.py` and the **original version** is stored in `models/ldgcnn_baseline.py`.

