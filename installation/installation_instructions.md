To plot the images presented in KITTI/Readme.md complete the following steps:
1. run:
```bash
git clone https://github.com/charlesq34/frustum-pointnets.git
```

2. Download the KITTI dataset from [KITTI website](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d)
   1. Unzip the files in the following directory structure: 
           dataset/KITTI/object/

            training/
                calib/
                image_2/
                label_2/ 
                velodyne/

            testing/
                calib/
                image_2/
                velodyne/ 
                
                
3. Install all requirements in the requirements.txt file:
```bash
pip install -r requirements.txt
```

4. Run:
```bash
python kitti_3d_exploration.py
```

5. For the Pedestrian detector, follow the tensorflow object_detection installation instructions at `https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md`
   1. After the object_detection installation is complete, run:

```bash 
python pedestrian_detector.py
```


