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

# Fonction pour charger une image
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        global current_image
        current_image = Image.open(file_path)
        update_display()

# Fonction pour effectuer une rotation de 90 degrés sur l'image
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

# Fonction pour charger une image dans le cadre actif sélectionné
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        global current_image
        current_image = Image.open(file_path)
        update()

# Fonction pour sauvegarder l'image dans le cadre actif sélectionné
def save_image():
    global current_image
    file_path = filedialog.asksaveasfilename(filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        current_image.save(file_path)

def update():
    global current_image, selected_frame
    if current_image:
        if selected_frame == img1_frame:
            update_display(image_label, current_image)
        elif selected_frame == img2_frame:
            update_display(image_label2, current_image)

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

# Fonction pour changer l'image affichée dans le cadre actif
def switch_image(frame):
    global current_image    
    #switch case impossible because we use python version inferior at 3.10
    if frame == img1_frame and images[0] != None:
        current_image = images[0]
    elif frame == img2_frame and images[1] != None:
        current_image = images[1]

            

# Fonction pour effectuer un zoom avant
def zoom_in():
    global zoom_factor
    zoom_factor += 0.1
    update()

# Fonction pour effectuer un zoom arrière
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