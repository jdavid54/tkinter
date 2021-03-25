#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        tkinter souris des boutons
# Purpose:
#
# Author:      Jean
#
# Created:     23/01/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

fenetre = Tk()

photo = PhotoImage(file="ma_photo.png")

canvas = Canvas(fenetre,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
mainloop()

def main():
    pass

if __name__ == '__main__':
    main()
