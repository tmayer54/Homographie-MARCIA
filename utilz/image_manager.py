#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 16:16:42 2023

@author : tmayer
"""

from PIL import Image, ImageTk
from tkinter import filedialog

class ImageManager:

    def __init__(self):
        self.current_image = None
        self.zoom_factor = 1.0
        self.images = [None, None]
        self.selected_frame = 1

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            self.images[self.selected_frame] = Image.open(file_path)
            self.current_image = self.images[self.selected_frame]

    def save_image(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
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

    def get_images(self):
        return self.images

    def get_selected_frame(self):
        return self.selected_frame

    def get_current_image(self):
        return self.current_image
    
    def get_zoom_factor(self):
        return self.zoom_factor
    
    def set_selected_frame(self, frame):
        self.selected_frame = frame

    """
        Function to switch the image displayed in the selected frame.

        This function switches the image displayed in the selected frame with the
        image stored in the 'images' list based on the selected frame. It checks if
        an image exists for the selected frame and updates the current image
        accordingly.

        Parameters:
            frame (tkinter.Frame): The frame for which to switch the image.

        Returns:
            None
    """
    def switch_image(self):
        #switch case impossible because we use python version inferior at 3.10
        if self.selected_frame == 0 and self.images[0] != None:
            self.current_image = self.images[0]
        elif self.selected_frame == 1 and self.images[1] != None:
            self.current_image = self.images[1]
    """
    Function to change the selected display frame.

    This function changes the currently selected display frame to the specified
    frame and updates the image displayed in the new frame accordingly.

    Parameters:
        frame (tkinter.Frame): The frame to be set as the selected frame.

    Returns:"
        None
    """
    def change_selected_frame(self, frame):
        self.selected_frame = frame
        self.switch_image()