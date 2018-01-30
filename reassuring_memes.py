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
def reassuringMemesGenerator() :
    reassuringMemes = ["http://i0.kym-cdn.com/photos/images/facebook/001/185/889/218.jpg","https://cdn.shopify.com/s/files/1/0972/5474/files/9d891ea4dad4547389af15e45ba25d42.jpg?16699883088683802383", "https://i.pinimg.com/736x/d9/78/d3/d978d3d7891a11abfc758b8b397349c4--cute-funny-animals-funny-animal-pictures.jpg","https://pics.me.me/rember-wen-u-feel-scare-never-forget-ttimes-wen-u-18830148.png", "https://pics.me.me/if-youre-having-a-bad-day-this-should-help-23298539.png", "https://i.redditmedia.com/-OHwz2koIoDu9B16fgL_KXN-jBeSU6jXeQMx30q1qP4.jpg?w=640&s=e8b352c35cee2ccc36672e928321f604", "https://www.youtube.com/watch?v=b97oDlT4GeE"]
    webbrowser.open(reassuringMemes[randint(0, len(reassuringMemes) - 1)])
    print("Here's a reassuring meme for you.")
