#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     21/01/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Python 2             Python 3
Tkinter         →  tkinter
Tix             →  tkinter.tix
ttk             →  tkinter.ttk
tkMessageBox    →  tkinter.messagebox
tkColorChooser  →  tkinter.colorchooser
tkFileDialog    →  tkinter.filedialog
tkCommonDialog  →  tkinter.commondialog
tkSimpleDialog  →  tkinter.simpledialog
tkFont          →  tkinter.font
Tkdnd           →  tkinter.dnd
ScrolledText    →  tkinter.scrolledtext
"""
from tkinter import *



def callback():
    global texte1,texte2
    print ('callbackget=',entree.get())
    print ('callbackget=',e.get())

def quitte():
    global texte1, texte2
    texte1=entree.get()
    texte2=e.get()
    #print(texte1,texte2)
    fenetre.destroy()

def main():
    global entree, e, fenetre
    fenetre = Tk()

    label = Label(fenetre, text="Hello World")
    label.pack()


    # label
    label = Label(fenetre, text="Texte par défaut", bg="yellow")
    label.pack()
    # entrée
    value = StringVar(fenetre)
    value.set("texte par défaut")
    entree = Entry(fenetre, textvariable=value, width=30)
    entree.pack()
    print(entree.get())  #imprime avant l'affichage de la fenêtre

    v = StringVar()
    v.set("valeur par défaut")
    e = Entry(fenetre, textvariable=v, width=30)
    e.pack()

    #v.set("a default value")
    s = e.get()
    print(s)         #imprime avant l'affichage de la fenêtre


    # bouton de sortie
    bouton=Button(fenetre, text="Fermer", command=quitte)
    bouton.pack()
    #bouton obligatoire pour manier les champs texte des entries
    b = Button(fenetre, text="get", width=10, command=callback)
    b.pack()
    fenetre.mainloop()


if __name__ == '__main__':

    main()
    print("Sortie",texte1,texte2)
