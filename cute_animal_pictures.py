#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Esme E. Vazquez
 # Date: 03/22/17, edited on 1/23/18
 # Title: Get Through Today
 # Purpose: A program to cheer you up after a hard day.

#Importing random-integer function
from random import randint
#Importing webbrowser function
import webbrowser

#A function to pick a random URL for a cute animal picture and open that URL
def cuteAnimalPicturesGenerator() :
    cuteAnimals = ["https://s-media-cache-ak0.pinimg.com/736x/65/9f/5b/659f5bdc2708232b1827288c2b52ebce.jpg", "https://s-media-cache-ak0.pinimg.com/736x/ca/69/48/ca694804d87ff867b6cf7a0e43c5d5f1.jpg", "https://i.ytimg.com/vi/Qa9JcoBVLgE/hqdefault.jpg", "https://i.pinimg.com/originals/f5/83/44/f58344aa6480ff1cc9c6253099b8331b.jpg", "https://static.boredpanda.com/blog/wp-content/uploads/2017/02/cute-animal-tongues-mlem-255-5899b9d5dcb97__700.jpg", "https://i.ytimg.com/vi/mXHbj_1A1p4/hqdefault.jpg"]
    webbrowser.open(cuteAnimals[randint(0, len(cuteAnimals) - 1)])
    print("Here's a cute animal.")
    
