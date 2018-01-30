#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 # Author: Esme E. Vazquez
 # Date: 03/22/17, edited on 1/23/18
 # Title: Get Through Today
 # Purpose: A program to cheer you up after a hard day.


#a file that generates a web address to a self care activity
import self_care_tips

#a file to trigger the web address of cute animal pictures
import cute_animal_pictures

#a file to trigger the web address of a funny video
import funny_videos

#a file to trigger the web address of a reassuring memes
import reassuring_memes

#a file to trigger a random word of encouragement
import words_of_encouragement

#to exit the program
import sys

#Create a program that will get you through today
#The goal of this program is to cheer up even the saddest person!

#A welcome message
welcome = print("\n Welcome! I am here to help you get through today!")

#Asks for the user's name
name = input("\n Who am I speaking to? " )

#The computer asks whats wrong, user provides response
#takes user input
answer = input("\n What's wrong, %s? Please select from below: \n \n 1. I am feeling sad. "
               "\n 2. I am feeling angry. "
               "\n 3. I am feeling insecure. "
               "\n 4. No worries, I am feeling much better now! \n" %(name))

#user responds with sadness
if int(answer) == 1:
    print("It's okay %s, you can get through today. One step at a time, everything is temporary. \n" %(name))
#user responds with anger
elif int(answer) == 2:
    print("%s, anger is a very powerful motivator, I hope you can use it as an equalizer in your life to overcome your challenges.\n" %(name))
#user responds with insecurity
elif int(answer) == 3:
    print("%s, insecurity can be minimized by some perspective, evaluate how lucky you are to be alive, and everything you are grateful for.\n " %(name))

#user says they are feeling better
elif int(answer) == 4:
   print("I am proud of your resilience %s. I suppose we are done here!" %(name))
   sys.exit()

#The computer offers help
help = input("How can I be of assistance %s? Please select from below: \n"
            "\n 1. I need some suggestions for self care."
            "\n 2. I need some cute animal pictures."
            "\n 3. I need some some funny videos."
            "\n 4. I need some reassuring memes."
            "\n 5. I need words of encouragement." 
            "\n 6. I don't need anything, thanks! \n" %(name))

while int(help) <= 6:

    #If the user asks for self care tips
    if int(help) == 1:
        self_care_tips.selfCareTipsGenerator()

    #If the user asks for cute animal pictures
    if int(help) == 2:
        cute_animal_pictures.cuteAnimalPicturesGenerator()

    #If the user asks for funny videos
    elif int(help) == 3:
        funny_videos.funnyVideosGenerator()

    #If the user asks for reassuring memes
    elif int(help) == 4:
        reassuring_memes.reassuringMemesGenerator()

    #If the user asks for words of encouragement
    elif int(help) == 5:
        words_of_encouragement.wordsOfEncouragmentGenerator()

    # If the user does not need help
    elif int(help) == 6:
        print("I am glad you don't need my help, you are a tough person %s." % (name))
        sys.exit()

    #The computer asks if you need anymore help
    furtherHelp = input("\n Would you like any further assistance %s? \n"
            "\n 1. Yes"
            "\n 2. No \n" %(name))

    if int(furtherHelp) == 1:

        # The computer offers help
        help = input("How can I be of assistance %s? Please select from below: \n"
                    "\n 1. I need some suggestions for self care."
                    "\n 2. I need some cute animal pictures."
                    "\n 3. I need some some funny videos."
                    "\n 4. I need some reassuring memes."
                    "\n 5. I need words of encouragement."
                    "\n 6. I don't need anything, thanks! \n" % (name))

    elif int(furtherHelp) == 2:

        print("I am glad you don't need my help, you are a tough person %s." % (name))
        sys.exit()


