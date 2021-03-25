#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
# http://tkinter.fdex.eu/doc/scw.html
# Created:     23/01/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

def affiche(valeur):     #la valeur de scale est donnée à l'appel
    #valeur=scale.get()     #pas de besoin de get
    print(valeur)

fenetre = Tk()
#scale
"""
Construct a scale widget with the parent MASTER.

Valid resource names: activebackground, background, bigincrement, bd,
bg, borderwidth, command, cursor, digits, fg, font, foreground, from,
highlightbackground, highlightcolor, highlightthickness, label,
length, orient, relief, repeatdelay, repeatinterval, resolution,
showvalue, sliderlength, sliderrelief, state, takefocus,
tickinterval, to, troughcolor, variable, width.
"""
value = DoubleVar()
scale = Scale(fenetre, variable=value, from_=10, to=42, orient='horizontal',command=affiche, label='num:')
scale.pack()

mainloop()

def main():
    pass

if __name__ == '__main__':
    main()
