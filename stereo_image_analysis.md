# Stereo Image Analysis

The KITTI dataset provides stereo images that are recorded by the two cameras that are mounted on the car. 
each image taken during the car ride is saved in two files (right and left). 
The stereo image capture can be used to build a 3D representation of the environment in front of the car using a technique that is similar to biological binocular vision.

Let's see an example of combinig two images (left and right) to one 3d image:


![left](images/disparity_analysis_left_image.png)
Right Image

![right](images/disparity_analysis_right_image.png)
Left Image

![right](images/disparity_analysis.png)
Disparity analysis

Looking at the example, it is clear that the person is located in different lcoations in the frame, on the right image the person it closer to the right than on the left image. The change in y axis depends on the actual distance between the cameras on the car.

Now let's compare the disparity analysis to the LIDAR capture of the same frame:

![LIDAR_no_box](images/LIDAR_no_box.png)
