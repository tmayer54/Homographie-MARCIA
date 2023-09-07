#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 16:21:18 2023

@author : tmayer
"""
from tkinter import Tk
from typing import Any
from UI.layout import setup_ui
from image_operations import initialize_image_operations

class UI_Manager:

    def __init__(self):
        self.root = Tk()
        self.root.title("MARCIA")
        self.root.geometry("1200x730")

    def setup_ui(self):
        setup_ui(self.root)
    
    def initialize_image_operations(self):
        initialize_image_operations(self.root)

    def start(self):
        self.root.mainloop()

    def getRoot(self):
        return self.root