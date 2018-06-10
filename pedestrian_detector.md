# Pedestrian Detector

Using object detection in tensorflow, I built a prototipe of pedestrian detector.
The object detection algorithm, which was trained on the KITTI dataset, detects cars, pedestrian, cyclists etc. My pedestrian detector 
will focus on detecting pedestrians that are in front of the car and are close enough. 

Let's define what "in front of the car" means. The object detector generates for each image the coordinates of the surrounding box 
for each of the identified subjects. Pedestrians that may require emergency-break would be between 0.25 and 0.75 of the horizontal axis 
of the frame (y).
Let's define what "close" means. Close pedestrians would apear bigger in the frame (take more space of the total frame). Object that are 
high enough would be considered as close. High is defined as `xmax-xmin>0.4`

Example: 

![pedestrian_warning](images/close_pedestrian.png)
## Close Pedestrian

![pedestrian_no_warning](images/far_pedestrian.png)
## Close Pedestrian
