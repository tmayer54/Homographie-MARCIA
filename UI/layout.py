#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 14:21:21 2023

@author : tmayer
"""
from tkinter import *
from image_operations import change_selected_frame, load_image, save_image, rotate_image, horizontal_flip, vertical_flip, zoom_in, zoom_out


def setup_ui(root):

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

    # Variable pour stocker l'image actuelle
    current_image = None
    images = [None, None]