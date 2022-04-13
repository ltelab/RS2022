#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:15:11 2022

@author: ghiggi
"""
from nbgitpuller_link import Link
git_https_url = "https://github.com/ltelab/RS2022"
dict_notebooks = {"Ex6": "exercice_6/Exercise_6.ipynb",
                  "Ex7": "exercice_7/Exercise_7.ipynb",
                 }
# Creation of the link
dict_noto_link = {}
for key, path_to_notebook in dict_notebooks.items():
    # Retrieve basic url 
    linker = Link(
        jupyterhub_url = "https://noto.epfl.ch",
        branch = "main",
        interface = "lab",
        repository_url = git_https_url,
        launch_path = path_to_notebook,
        )
    # Set cloning depth to 1
    url = linker.link + "&depth=1"
    
    # Add url to dictionary 
    dict_noto_link[key] = url

# Display of the link
print(dict_noto_link)
 