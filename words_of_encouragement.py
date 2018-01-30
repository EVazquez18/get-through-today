#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Esme E. Vazquez
 # Date: 03/22/17, edited on 1/23/18
 # Title: Get Through Today
 # Purpose: A program to cheer you up after a hard day.

#Importing random-integer function
from random import randint

#A function to pick a random URL for a cute animal picture and open that URL
def wordsOfEncouragmentGenerator() :
    wordsOfEncouragement = ["You are attractive.", "You are intelligent.", "You can get through this",
                            "You are a good person", "You've got heart", "I believe in you", "You've  "]
    print("Here's a word of encouragement: ")
    print(wordsOfEncouragement[randint(0, len(wordsOfEncouragement) - 1)])
