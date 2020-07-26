## Datasets

This folder stores the datasets shared by multiple networks to avoid redundancy.

To download the datasets, check out the instructions for [`launcher.py`](https://github.com/horizon-research/Efficient-Deep-Learning-for-Point-Clouds) or simply step back and run:
```
$ python launcher.py --download all
```
Below shows the relationship among model name, task type, and dataset name:

<table >
   <tr>
        <td>Actual Model Name</td>
        <td>Name in Our Code</td>
        <td>Task Type</td>
        <td>Dataset Name</td>
    <td>Folder Name</td>
   </tr>
   <tr>
        <td rowspan="2">PointNet++</td>
        <td rowspan="2">pointnet2</td>
        <td>Classification</td>
      <td>ModelNet</td>
    <td>modelnet40_ply...</td>
   </tr>
   <tr>
        <td>Segmentation</td>
        <td>ShapeNet</td>
    <td>shapenetcore...</td>
   </tr>
   <tr>
      <td rowspan="2">DGCNN</td>
      <td rowspan="2">dgcnn</td>
      <td>Classification</td>
      <td>ModelNet</td>
    <td>modelnet40_ply...</td>
   </tr>
   <tr>
      <td>Segmentation</td>
      <td>ShapeNet</td>
    <td>Part..., hdf5...</td>
   </tr>
   <tr>
      <td>LDGCNN</td>
      <td>ldgcnn</td>
      <td>Classification</td>
      <td>ModelNet</td>
    <td>modelnet40_ply...</td>
   </tr>
   <tr>
      <td>F-PointNet</td>
      <td>frustum-pointnets</td>
      <td>3D Detection</td>
      <td>KITTI</td>
    <td></td>
   </tr>
   <tr>
      <td>DensePoint</td>
      <td>DensePoint</td>
      <td>Classification</td>
      <td>ModelNet</td>
    <td>modelnet40_ply...</td>
   </tr>
</table>