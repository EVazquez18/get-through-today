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
def funnyVideosGenerator() :
    funnyVideos = [ "https://www.youtube.com/watch?v=C1pkVrHKDik", "https://www.youtube.com/watch?v=Mh4f9AYRCZY&feature=youtu.be","https://www.youtube.com/watch?v=4WgT9gy4zQA", "https://www.youtube.com/watch?v=fKGoVefhtMQ"]
    webbrowser.open(funnyVideos[randint(0,len(funnyVideos) - 1)])
    print("Here's a funny video for you.")
