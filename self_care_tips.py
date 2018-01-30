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
def selfCareTipsGenerator() :
    selfCare = ["Take a long, hot shower or bath", "Take a morning walk.", "Spend some time outside in nature.", "Take a short nap.", "Learn to meditate.", "Write down an idea you've had and expand upon it.", "Have lunch in a park.", "Visit a local museum.", "Declutter your space."]

    print("Here's a self care activity:")
    print(selfCare[randint(0, len(selfCare) - 1)])
