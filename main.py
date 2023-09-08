#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 14:10:37 2023

@author : tmayer
"""

from PIL import ImageTk
from UI.ui_manager import UI_Manager
from utilz.image_manager import ImageManager
            

if __name__ == "__main__":
    print("Début du programme")
    ui_manager = UI_Manager()
    ui_manager.start()
    print("Fin du programme")