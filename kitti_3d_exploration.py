import os
import sys
import numpy as np
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'mayavi'))
from kitti_object import *

def my_data_vis():
    dataset = kitti_object(os.path.join(ROOT_DIR, 'dataset/KITTI/object'))

    for data_idx in [0,2,4,6]:
        # Load data from dataset
        objects = dataset.get_label_objects(data_idx)
        objects[0].print_object()
        img = dataset.get_image(data_idx)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_height, img_width, img_channel = img.shape


        print(('Image shape: ', img.shape))
        pc_velo = dataset.get_lidar(data_idx)[:, 0:3]
        calib = dataset.get_calibration(data_idx)

        # Draw 2d and 3d boxes on image
        show_image_with_boxes(img, objects, calib, False)
        raw_input()

        print('LIDAR without boxes')
        show_lidar(pc_velo, calib, True, img_width, img_height)
        raw_input()

        print('LIDAR with boxes')
        show_lidar_with_boxes(pc_velo, objects, calib, True, img_width, img_height)
        raw_input()

        print('noise LIDAR')
        pc_velo_with_noise = pc_velo + 0.3*np.random.rand(*pc_velo.shape)
        show_lidar_with_boxes(pc_velo_with_noise, objects, calib, True, img_width, img_height)
        raw_input()


if __name__=='__main__':

    my_data_vis()


