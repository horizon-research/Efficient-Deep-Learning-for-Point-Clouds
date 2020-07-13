#!/bin/bash

# Download original ShapeNetPart dataset (around 1GB) ['PartAnnotation']
wget https://shapenet.cs.stanford.edu/ericyi/shapenetcore_partanno_v0.zip --no-check-certificate
unzip shapenetcore_partanno_v0.zip
rm shapenetcore_partanno_v0.zip

# Download HDF5 for ShapeNet Part segmentation (around 346MB) ['hdf5_data']
wget https://shapenet.cs.stanford.edu/media/shapenet_part_seg_hdf5_data.zip --no-check-certificate
unzip shapenet_part_seg_hdf5_data.zip
rm shapenet_part_seg_hdf5_data.zip
