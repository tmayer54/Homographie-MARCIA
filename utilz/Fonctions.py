#!/usr/bin/env python3.8
import pandas as pd
from tkinter import *
from matplotlib.rcsetup import validate_color_for_prop_cycle, validate_color_or_auto
import tkinter as tk
from pyparsing import col
from PIL import Image, ImageTk
from tkinter import filedialog

# Fonction pour changer l'image affichée dans le cadre actif
def switch_image(frame, images):
    global current_image
    #switch case impossible because we use python version inferior at 3.10
    if frame == 1 and images[0] != None:
        current_image = images[0]
    elif frame == 2 and images[1] != None:
        current_image = images[1]

# Fonction pour effectuer une rotation de 90 degrés sur l'image
def rotate_image(labels):
    global current_image
    if current_image:
        current_image = current_image.rotate(90)
        update(labels)

def horizontal_flip(labels):
    global current_image
    current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
    update(labels)

def vertical_flip(labels):
    global current_image
    current_image = current_image.transpose(Image.FLIP_TOP_BOTTOM)
    update(labels)

# Fonction pour charger une image dans le cadre actif sélectionné
def load_image(labels):
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        global current_image
        current_image = Image.open(file_path)
        update(labels)

# Fonction pour sauvegarder l'image dans le cadre actif sélectionné
def save_image():
    global current_image
    file_path = filedialog.asksaveasfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        current_image.save(file_path)

def update(labels):
    global current_image, selected_frame
    if current_image:
        if selected_frame == 1:
            update_display(labels[0], current_image)
        elif selected_frame == 2:
            update_display(labels[1], current_image)
            
# Fonction pour mettre à jour l'affichage de l'image
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


# Fonction pour changer le cadre actif
def change_selected_frame(frame):
    global current_image, selected_frame
    selected_frame = frame
    switch_image(selected_frame)


# Fonction pour effectuer un zoom avant
def zoom_in(labels):
    global zoom_factor
    zoom_factor += 0.1
    update(labels)

# Fonction pour effectuer un zoom arrière
def zoom_out(labels):
    global zoom_factor
    zoom_factor -= 0.1
    if zoom_factor < 0.1:
        zoom_factor = 0.1
    update(labels)

