#/bin/bash
python2 train/test.py --gpu 0 --num_point 1024 \
	--model frustum_pointnets_v2 --model_path train/log_v2_baseline/model.ckpt \
        --output detection_results_v2 \
        --data_path kitti/frustum_carpedcyc_val_rgb_detection.pickle \
        --from_rgb_detection \
        --use_baseline True\
        --idx_path kitti/image_sets/val.txt

train/kitti_eval/evaluate_object_3d_offline \
                dataset/training/label_2/ \
                detection_results_v2
