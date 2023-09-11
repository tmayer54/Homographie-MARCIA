#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 16:21:18 2023

@author : tmayer
"""
from tkinter import *
from PIL import ImageTk
from utilz.image_manager import *

class UI_Manager:

    def __init__(self):
        self.root = Tk()
        self.root.title("MARCIA")
        self.root.geometry("1200x730")
        self.image_manager = ImageManager()
        self.image_label = None
        self.image_label2 = None
        self.mixtimg_label = None
        self.info1_label = None
        self.setup_ui()

    def setup_ui(self):

        #Créer les 4 cadre de l'interface graphique
        '''
        |-----------| |-----------|             |
        |img1_frame | |img2_frame |             |
        |-----------| |-----------|mixtimg_frame|
        |info1_frame| |info2_frame|             |
        |-----------| |-----------|             |
        '''

        img1_frame = Frame(self.root, borderwidth=2, relief="solid", width=375, height=375)
        img2_frame = Frame(self.root, borderwidth=2, relief="solid", width=375, height=375)
        info1_frame = Frame(self.root, borderwidth=2, relief="solid", width=375, height=375)
        info2_frame = Frame(self.root, borderwidth=2, relief="solid", width=375, height=375)
        mixtimg_frame = Frame(self.root, borderwidth=2, relief="solid", width=400, height=830)

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
        frame_selection_label = Label(self.root, text="Sélectionner le cadre actif:")
        frame_selection_label.grid(row=0, column=0, columnspan=2)
        img1_button = Radiobutton(self.root, text="Image 1", variable=selected_frame, value=img1_frame, command=lambda:self.image_manager.change_selected_frame(0))
        img2_button = Radiobutton(self.root, text="Image 2", variable=selected_frame, value=img2_frame, command=lambda:self.image_manager.change_selected_frame(1))
        img1_button.grid(row=0, column=2)
        img2_button.grid(row=0, column=3)

        # Créer une étiquette pour afficher l'image (vide au départ)
        self.image_label = Label(img1_frame)
        self.image_label.pack()

        # Créer une étiquette pour afficher l'image dans img2_frame
        self.image_label2 = Label(img2_frame)
        self.image_label2.pack()

        # Créer une étiquette pour afficher l'image mixée
        mixtimg_label = Label(mixtimg_frame)
        mixtimg_label.pack()

        # Créer une étiquette pour afficher les informations de l'image 1
        self.info1_label = Label(info1_frame, text="test")
        self.info1_label.pack()

        #Création du Menu
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Ouvrir", command=self.load_image)
        filemenu.add_command(label="Enregistrer", command=self.save_image)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=self.root.quit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="Fichier", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Rotation", command=self.rotate_image, accelerator="Ctrl+right")
        editmenu.add_command(label="Horizontal flip", command=self.horizontal_flip, accelerator="Ctrl+left")
        editmenu.add_command(label="Vertical flip", command=self.vertical_flip, accelerator="Ctrl+up")
        editmenu.add_separator()
        editmenu.add_command(label="Zoom avant", command=self.zoom_in, accelerator="Ctrl++")
        editmenu.add_command(label="Zoom arrière", command=self.zoom_out, accelerator="Ctrl+-")
        menubar.add_cascade(label="Edition", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="A propos")
        menubar.add_cascade(label="Aide", menu=helpmenu)

        self.root.config(menu=menubar)
        self.root.bind('<Control-Right>', lambda event:self.rotate_image())
        self.root.bind('<Control-Left>', lambda event:self.horizontal_flip())
        self.root.bind('<Control-Up>', lambda event:self.vertical_flip())
        self.root.bind('<Control-q>', lambda event:self.root.quit())
        self.root.bind('<Control-plus>', lambda event:self.zoom_in())
        self.root.bind('<Control-minus>', lambda event:self.zoom_out())
        self.root.bind('<Button-1>', lambda event:self.on_click)

    """
        Function to update the display with the current image.

        This function updates the display in the selected frame with the current
        image.

        Parameters:
            None

        Returns:
            None
    """
    def update(self):
        if self.image_manager.get_current_image():
            if self.image_manager.get_selected_frame() == 0:
                self.update_display()
            elif self.image_manager.get_selected_frame()  == 1:
                self.update_display()
    
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
    def update_display(self):
        if self.image_manager.get_current_image():
            # Redimensionner l'image
            width, height = self.image_manager.get_current_image().size
            new_width = int(width * self.image_manager.get_zoom_factor(self.image_manager.get_selected_frame()))
            new_height = int(height * self.image_manager.get_zoom_factor(self.image_manager.get_selected_frame()))
            resized_image = self.image_manager.get_current_image().resize((new_width, new_height))
            # Afficher l'image dans le bon cadre
            photo = ImageTk.PhotoImage(resized_image)
            if self.image_manager.get_selected_frame() == 0:
                frame = self.image_label
            elif self.image_manager.get_selected_frame() == 1:
                frame = self.image_label2
            frame.config(image=photo)
            frame.image = photo

    def load_image(self):
        self.image_manager.load_image()
        self.update()

    def save_image(self):
        self.image_manager.save_image()

    def rotate_image(self):
        self.image_manager.rotate_image()
        self.update()
    
    def horizontal_flip(self):
        self.image_manager.horizontal_flip()
        self.update()

    def vertical_flip(self):
        self.image_manager.vertical_flip()
        self.update()
    
    def zoom_in(self):
        self.image_manager.zoom_in()
        self.update()

    def zoom_out(self):
        self.image_manager.zoom_out()
        self.update()
    
    def on_click(self,event):
        x, y = event.x, event.y
        self.info1_label.config(text=f"Mouse clicked at X: {x}, Y: {y}")

    def start(self):
        self.root.mainloop()

    def getRoot(self):
        return self.root