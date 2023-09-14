#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 08:06:58 2023

@author: korbel1
"""

import cv2
import numpy as np
 
 
if __name__ == '__main__' :
 
    # Read source image.
    im_src = cv2.imread('modified.jpg')
    # Four corners of the book in source image
    pts_src = np.array([[0, 299], [599, 299], [0, 0], [599, 0]])
 
    # Read destination image.
    im_dst = cv2.imread('base.jpg')
    # Four corners of the book in destination image.
    pts_dst = np.array([[0,0],[999, 0], [0, 999], [999, 999]])
 
    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    print (h)
    print (status)
    
    print(im_dst.shape[1])
 
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
 
    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)
    
    cv2.imwrite("result.jpg",im_out)