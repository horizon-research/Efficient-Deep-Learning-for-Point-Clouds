#/bin/bash

BATCH_SIZE=8

python train/train.py --gpu 1 --model frustum_pointnets_v2 \
    --log_dir train/log_v2_limited --num_point 1024 --max_epoch 201 \
    --batch_size ${BATCH_SIZE} --decay_step 800000 --decay_rate 0.5 \
    --use_limited True
