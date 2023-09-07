#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 14:10:37 2023

@author : tmayer
"""


# main.py
from tkinter import Tk
from UI.layout import setup_ui

if __name__ == "__main__":
    root = Tk()
    root.title("MARCIA")
    root.geometry("1200x730")
    
    # Initialize the UI layout
    setup_ui(root)
    
    # Initialize image operations
    initialize_image_operations(root)
    
    # Start the main application loop
    root.mainloop()