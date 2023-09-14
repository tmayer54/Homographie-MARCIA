#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""i
Created on Wed Sept 13 16:16:58 2023

@author: tmayer
"""
import cv2
from image_similarity_measures.quality_metrics import rmse

in_img1 = cv2.imread('base.jpg')
in_img2 = cv2.imread('result.jpg')

out_rmse = rmse(in_img1, in_img2)
