#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 16:16:42 2023

@author : tmayer
"""

from PIL import Image
from tkinter import filedialog

class ImageManager:

    def __init__(self):
        self.current_image = None
        self.zoom_factor = [1,1]
        self.images = [None, None]
        self.coords = [[None, None, None, None], [None, None, None, None]]
        self.selected_frame = 0


    """
        Function to load an image from a file dialog.

        This function opens a file dialog allowing the user to select an image file
        (JPEG, PNG, GIF, BMP) and then loads and displays the selected image.

        Parameters:
            None

        Returns:
            None
    """
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            self.images[self.selected_frame] = Image.open(file_path)
            self.current_image = self.images[self.selected_frame]

    """
        Function to save the current image to a file.

        This function opens a file dialog allowing the user to specify a file name
        and location to save the current image. It then saves the image in the
        selected format (JPEG, PNG, GIF, BMP).

        Parameters:
            None

        Returns:
            None
    """
    def save_image(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if self.current_image and file_path:
            self.current_image.save(file_path)

    """
        Function to rotate the current image 90 degrees clockwise.

        This function rotates the currently loaded image 90 degrees clockwise and
        updates the display with the rotated image.

        Parameters:
            None

        Returns:
            None
    """
    def rotate_image(self):
        if self.current_image:
            self.current_image = self.current_image.rotate(90)

    """
        Function to horizontally flip the current image.

        This function flips the currently loaded image horizontally (left to right)
        and updates the display with the flipped image.

        Parameters:
            None

        Returns:
            None
    """
    def horizontal_flip(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT)

    """
        Function to vertically flip the current image.

        This function flips the currently loaded image vertically (top to bottom)
        and updates the display with the flipped image.

        Parameters:
            None

        Returns:
            None
    """
    def vertical_flip(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.FLIP_TOP_BOTTOM)

    """
        Function to zoom in on the current image.

        This function increases the zoom factor by 0.1 and updates the display with
        the zoomed-in image.

        Parameters:
            None

        Returns:
            None
    """
    def zoom_in(self):
        self.zoom_factor[self.selected_frame] += 0.1

    """
        Function to zoom out from the current image.

        This function decreases the zoom factor by 0.1 and updates the display with
        the zoomed-out image. The zoom factor cannot go below 0.1.

        Parameters:
            None

        Returns:
            None
    """
    def zoom_out(self):
        self.zoom_factor[self.selected_frame] -= 0.1
        if self.zoom_factor[self.selected_frame] < 0.1:
            self.zoom_factor[self.selected_frame] = 0.1


    """
    Getters & Setters
    """
    def get_images(self):
        return self.images

    def get_selected_frame(self):
        return self.selected_frame

    def get_current_image(self):
        return self.current_image
    
    def get_zoom_factor(self, frame):
        return self.zoom_factor[frame]
    
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

    Returns:
        None
    """
    def change_selected_frame(self, frame):
        self.selected_frame = frame
        self.switch_image()

    """
        Function to add a coordinate to the list of coordinates of the current image

        Parameters:
            coords (list): coordinate to be added

        Returns:
            None
    """    
    def add_coords(self, coords):
        for coord in self.coords[self.selected_frame]:
            if coord == None:
                coord = coords
                break
        print("Already 4 coords")   #DEBUG
    
    """
        Function to reset the list of coordinates of the current image

        Parameters:
            None

        Returns:
            None
    """
    def remove_coords(self):
        self.coords[self.selected_frame] = [None, None, None, None]
