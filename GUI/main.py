#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Thu Sept 7 14:10:37 2023

@author : tmayer
"""

from UI.ui_manager import UI_Manager

if __name__ == "__main__":
    print("----------Début du programme----------")
    print("----------Lancement de l'interface graphique----------")
    ui_manager = UI_Manager()
    print("----------Interface graphique chargée----------")
    ui_manager.start()
    print("----------Fin du programme----------")