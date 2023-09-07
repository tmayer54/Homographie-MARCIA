#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 16:16:42 2023

@author : tmayer
"""

from PIL import Image, ImageTk

class ImageManager:

    def __init__(self):
        self.current_image = None
        self.zoom_factor = 1.0
        self.images = [None, None]

    def load_image(self, file_path, selected_frame):
        if file_path:
            self.images[selected_frame] = Image.open(file_path)

    def save_image(self, file_path):
        if self.current_image and file_path:
            self.current_image.save(file_path)

    def rotate_image(self):
        if self.current_image:
            self.current_image = self.current_image.rotate(90)

    def horizontal_flip(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT)

    def vertical_flip(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.FLIP_TOP_BOTTOM)

    def zoom_in(self):
        self.zoom_factor += 0.1

    def zoom_out(self):
        self.zoom_factor -= 0.1
        if self.zoom_factor < 0.1:
            self.zoom_factor = 0.1