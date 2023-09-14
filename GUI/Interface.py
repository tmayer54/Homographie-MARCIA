#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on We Sept 6 15:10:37 2023

@author : tmayer
"""
import pandas as pd
from tkinter import *
from matplotlib.rcsetup import validate_color_for_prop_cycle, validate_color_or_auto
import tkinter as tk
from pyparsing import col
from PIL import Image, ImageTk
from tkinter import filedialog


#INIT : 
zoom_factor = 1.0

"""
    Function to load an image from a file dialog.

    This function opens a file dialog allowing the user to select an image file
    (JPEG, PNG, GIF, BMP) and then loads and displays the selected image.

    Parameters:
        None

    Returns:
        None
"""
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        global current_image, selected_frame
        current_image = Image.open(file_path)
        if selected_frame == img1_frame:
            images[0] = current_image
        elif selected_frame == img2_frame:
            images[1] = current_image
        update()

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
def save_image():
    global current_image
    file_path = filedialog.asksaveasfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        current_image.save(file_path)


"""
    Function to rotate the current image 90 degrees clockwise.

    This function rotates the currently loaded image 90 degrees clockwise and
    updates the display with the rotated image.

    Parameters:
        None

    Returns:
        None
"""
def rotate_image():
    global current_image
    if current_image:
        current_image = current_image.rotate(90)
        update()

"""
    Function to horizontally flip the current image.

    This function flips the currently loaded image horizontally (left to right)
    and updates the display with the flipped image.

    Parameters:
        None

    Returns:
        None
"""
def horizontal_flip():
    global current_image
    current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
    update()

"""
    Function to vertically flip the current image.

    This function flips the currently loaded image vertically (top to bottom)
    and updates the display with the flipped image.

    Parameters:
        None

    Returns:
        None
"""
def vertical_flip():
    global current_image
    current_image = current_image.transpose(Image.FLIP_TOP_BOTTOM)
    update()

"""
    Function to update the display with the current image.

    This function updates the display in the selected frame with the current
    image.

    Parameters:
        None

    Returns:
        None
"""
def update():
    global current_image, selected_frame
    if current_image:
        if selected_frame == img1_frame:
            update_display(image_label, current_image)
        elif selected_frame == img2_frame:
            update_display(image_label2, current_image)

"""
    Function to update the display frame with the given image.

    This function resizes the given image according to the zoom factor and
    updates the specified display frame with the resized image.

    Parameters:
        frame (tkinter.Frame): The frame in which to display the image.
        image (PIL.Image.Image): The image to be displayed.

    Returns:
        None
"""
def update_display(frame, image):
    if image:
        # Redimensionner l'image
        width, height = image.size
        new_width = int(width * zoom_factor)
        new_height = int(height * zoom_factor)
        resized_image = image.resize((new_width, new_height))
        # Afficher l'image dans le cadre
        photo = ImageTk.PhotoImage(resized_image)
        frame.config(image=photo)
        frame.image = photo


"""
    Function to change the selected display frame.

    This function changes the currently selected display frame to the specified
    frame and updates the image displayed in the new frame accordingly.

    Parameters:
        frame (tkinter.Frame): The frame to be set as the selected frame.

    Returns:
        None
"""
def change_selected_frame(frame):
    global current_image, selected_frame
    selected_frame = frame
    switch_image(selected_frame)

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
def switch_image(frame):
    global current_image    
    #switch case impossible because we use python version inferior at 3.10
    if frame == img1_frame and images[0] != None:
        current_image = images[0]
    elif frame == img2_frame and images[1] != None:
        current_image = images[1]

            
"""
    Function to zoom in on the current image.

    This function increases the zoom factor by 0.1 and updates the display with
    the zoomed-in image.

    Parameters:
        None

    Returns:
        None
"""
def zoom_in():
    global zoom_factor
    zoom_factor += 0.1
    update()

"""
    Function to zoom out from the current image.

    This function decreases the zoom factor by 0.1 and updates the display with
    the zoomed-out image. The zoom factor cannot go below 0.1.

    Parameters:
        None

    Returns:
        None
"""
def zoom_out():
    global zoom_factor
    zoom_factor -= 0.1
    if zoom_factor < 0.1:
        zoom_factor = 0.1
    update()

# Créer une fenêtre principale
root = Tk() 
root.title("MARCIA")
root.geometry("1200x730")


#Création du Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Ouvrir", command=load_image)
filemenu.add_command(label="Enregistrer", command=save_image)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Fichier", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Rotation", command=rotate_image)
editmenu.add_command(label="Horizontal flip", command=horizontal_flip)
editmenu.add_command(label="Vertical flip", command=vertical_flip)
editmenu.add_separator()
editmenu.add_command(label="Zoom avant", command=zoom_in)
editmenu.add_command(label="Zoom arrière", command=zoom_out)
menubar.add_cascade(label="Edition", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="A propos")
menubar.add_cascade(label="Aide", menu=helpmenu)

root.config(menu=menubar)

#Créer les 4 cadre de l'interface graphique
'''
|-----------| |-----------|             |
|img1_frame | |img2_frame |             |
|-----------| |-----------|mixtimg_frame|
|info1_frame| |info2_frame|             |
|-----------| |-----------|             |
'''

img1_frame = Frame(root, borderwidth=2, relief="solid", width=375, height=375)
img2_frame = Frame(root, borderwidth=2, relief="solid", width=375, height=375)
info1_frame = Frame(root, borderwidth=2, relief="solid", width=375, height=375)
info2_frame = Frame(root, borderwidth=2, relief="solid", width=375, height=375)
mixtimg_frame = Frame(root, borderwidth=2, relief="solid", width=400, height=830)

# Répartir les colonnes en utilisant la méthode grid
img1_frame.grid(row=1, column=0, sticky="nsew")
img1_frame.pack_propagate(False)
img2_frame.grid(row=1, column=1, sticky="nsew")
img2_frame.pack_propagate(False)
info1_frame.grid(row=2, column=0, sticky="nsew")
info2_frame.grid(row=2, column=1, sticky="nsew")
mixtimg_frame.grid(row=1, rowspan=2, column=2, sticky="nsew")
mixtimg_frame.pack_propagate(False)

# Créer les boutons radio pour sélectionner le cadre actif
selected_frame = img1_frame  # Par défaut, img1_frame est sélectionné
frame_selection_label = Label(root, text="Sélectionner le cadre actif:")
frame_selection_label.grid(row=0, column=0, columnspan=2)
img1_button = Radiobutton(root, text="Image 1", variable=selected_frame, value=img1_frame, command=lambda: change_selected_frame(img1_frame))
img2_button = Radiobutton(root, text="Image 2", variable=selected_frame, value=img2_frame, command=lambda: change_selected_frame(img2_frame))
img1_button.grid(row=0, column=2)
img2_button.grid(row=0, column=3)


# Charger l'icône "save.png"
icon_save = PhotoImage(file="images/save.png")
icon_save = icon_save.zoom(1)

# Charger l'icône "folder.png"
icon_open = PhotoImage(file="images/file.png")
icon_open = icon_open.zoom(1)

# Charger l'icône "plus.png"
icon_plus = PhotoImage(file="images/plus.png")
icon_plus = icon_plus.zoom(1)

# Créer une étiquette pour afficher l'image (vide au départ)
image_label = Label(img1_frame)
image_label.pack()

# Créer une étiquette pour afficher l'image dans img2_frame
image_label2 = Label(img2_frame)
image_label2.pack()

# Créer une étiquette pour afficher l'image mixée
mixtimg_label = Label(mixtimg_frame)
mixtimg_label.pack()

# Variable pour stocker l'image actuelle
current_image = None
images = [None, None]

# Démarrer la boucle principale de l'interface graphique
root.mainloop()