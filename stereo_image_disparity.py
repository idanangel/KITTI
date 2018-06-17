import numpy as np
from sklearn.preprocessing import normalize
import cv2
import os

imgL_path = '/home/idan/KITTI/downloaded_data/images/training/image_2/'
imgR_path = '/home/idan/KITTI/downloaded_data/images/training/image_3/'
image_file_name = '000000.png'


def plotDisparityMap(left_image_path,
                     right_image_path,
                     applyWlsFilter=False,
                     sgbm_window_size=3,
                     sgbm_minDisparity=0,
                     sgbm_numDisparities=160,
                     sgbm_blockSize=5,
                     sgbm_disp12MaxDiff=1,
                     sgbm_uniquenessRatio=15,
                     sgbm_speckleWindowSize=0,
                     sgbm_speckleRange=2,
                     sgbm_preFilterCap=63,
                     sgbm_mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY):

    print('loading images...')
    imgL = cv2.imread(left_image_path)
    imgR = cv2.imread(right_image_path)

    left_matcher = cv2.StereoSGBM_create(
        minDisparity=sgbm_minDisparity,
        numDisparities=sgbm_numDisparities,
        blockSize=sgbm_blockSize,
        P1=8 * 3 * sgbm_window_size ** 2,   
        P2=32 * 3 * sgbm_window_size ** 2,
        disp12MaxDiff=sgbm_disp12MaxDiff,
        uniquenessRatio=sgbm_uniquenessRatio,
        speckleWindowSize=sgbm_speckleWindowSize,
        speckleRange=sgbm_speckleRange,
        preFilterCap=sgbm_preFilterCap,
        mode=sgbm_mode
    )

    right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)

    # FILTER Parameters
    lmbda = 80000
    sigma = 1.2

    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=left_matcher)
    wls_filter.setLambda(lmbda)
    wls_filter.setSigmaColor(sigma)

    print('computing disparity...')
    displ = left_matcher.compute(imgL, imgR)
    dispr = right_matcher.compute(imgR, imgL)
    displ = np.int16(displ)
    dispr = np.int16(dispr)


    if applyWlsFilter:
        filteredImg = wls_filter.filter(displ, imgL, None, dispr)
        filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX);
        filteredImg = np.uint8(filteredImg)
        cv2.imshow('Disparity Map', filteredImg)
    else:
        cv2.imshow('Disparity Map', displ)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    imgL_path = '/home/idan/KITTI/downloaded_data/images/training/image_2/'
    imgR_path = '/home/idan/KITTI/downloaded_data/images/training/image_3/'
    image_file_name = '000000.png'


    # Plot disparity map without WLS filter
    plotDisparityMap(os.path.join(imgL_path, image_file_name),
                     os.path.join(imgR_path, image_file_name),
                     applyWlsFilter=False,
                     sgbm_window_size=3,
                     sgbm_minDisparity=0,
                     sgbm_numDisparities=160,
                     sgbm_blockSize=5,
                     sgbm_disp12MaxDiff=1,
                     sgbm_uniquenessRatio=15,
                     sgbm_speckleWindowSize=0,
                     sgbm_speckleRange=2,
                     sgbm_preFilterCap=63,
                     sgbm_mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
                     )

    # Plot disparity map with WLS filter
    plotDisparityMap(os.path.join(imgL_path, image_file_name),
                     os.path.join(imgR_path, image_file_name),
                     applyWlsFilter=True,
                     sgbm_window_size=3,
                     sgbm_minDisparity=0,
                     sgbm_numDisparities=160,
                     sgbm_blockSize=5,
                     sgbm_disp12MaxDiff=1,
                     sgbm_uniquenessRatio=15,
                     sgbm_speckleWindowSize=0,
                     sgbm_speckleRange=2,
                     sgbm_preFilterCap=63,
                     sgbm_mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
                     )