# -*- coding: utf-8 -*-
#!/usr/bin/python
# Python2.7.14 -- SQLite3 -- TCLTK 8.5.18 -- macOS 10.12.6 (Sierra) -- Darwin

#Fizzbuzz challenge 16Nov2017

import math

def Jackpot():
    fzBzInput = int(input("Please enter a whole number: "))
    
    if (fzBzInput%3 == 0) and (fzBzInput%5 == 0):
        print ("Fizzbuzz!")
    elif fzBzInput%3 == 0:
        print ("Fizzledizzleroo")
    elif fzBzInput%5 == 0:
        print ("Buzzeroo")
    else:
        print ("Thanks for playing! Mountain Dew is the only fizz or buzz for you today.")


Jackpot()
