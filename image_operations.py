#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 15:11:05 2023

@author : tmayer
"""
from tkinter import filedialog, Menu
from tkinter import filedialog
from PIL import Image, ImageTk
from utilz.Fonctions import update
from utilz.image_manager import ImageManager

def initialize_image_operations(root):

    # Create the image manager
    image_manager = ImageManager()

    # Create a function to open the file dialog and load an image
    def load_image():
        image_manager.load_image(filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")]), selected_frame)
        update()

    def save_image():
        global current_image
        file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            current_image.save(file_path)

    def rotate_image():
        global current_image
        if current_image:
            current_image = current_image.rotate(90)
            update()

    def horizontal_flip():
        global current_image
        current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
        update()

    def vertical_flip():
        global current_image
        current_image = current_image.transpose(Image.FLIP_TOP_BOTTOM)
        update()

    def zoom_in():
        global zoom_factor
        zoom_factor += 0.1
        update()

    def zoom_out():
        global zoom_factor
        zoom_factor -= 0.1
        if zoom_factor < 0.1:
            zoom_factor = 0.1
        update()

    # Create the "File" menu
    file_menu = Menu(root)
    file_menu.add_command(label="Open", command=load_image)
    file_menu.add_command(label="Save", command=save_image)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Create the "Edit" menu
    edit_menu = Menu(root)
    edit_menu.add_command(label="Rotate", command=rotate_image)
    edit_menu.add_command(label="Horizontal Flip", command=horizontal_flip)
    edit_menu.add_command(label="Vertical Flip", command=vertical_flip)
    edit_menu.add_separator()
    edit_menu.add_command(label="Zoom In", command=zoom_in)
    edit_menu.add_command(label="Zoom Out", command=zoom_out)

    # Create the main menu bar
    main_menu = Menu(root)
    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Edit", menu=edit_menu)

    # Configure the main menu bar
    root.config(menu=main_menu)

    images = [None, None]
