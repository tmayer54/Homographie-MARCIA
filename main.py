#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 14:10:37 2023

@author : tmayer
"""

from utilz.ui_manager import UI_Manager

if __name__ == "__main__":

    ui_manager = UI_Manager()
    ui_manager.setup_ui()
    ui_manager.initialize_image_operations()
    ui_manager.start()