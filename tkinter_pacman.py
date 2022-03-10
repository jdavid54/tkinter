#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *

import random

vit_x = 10

vit_y = 0

vit_x2 = -10

vit_y2 = 0

animation_active = False

stop_animation = False


# ----------------------------------------------------------------

# Fonctions

# ----------------------------------------------------------------

def modification():

    global vit_x

    global vit_y

    global animation_active

    global stop_animation

    animation_active = True

    mod_angle = 0

    liste_coord = monCanvas.coords(pacman_1)

    liste_items = monCanvas.find_overlapping(liste_coord[0],liste_coord[1],liste_coord[2],liste_coord[3])

    test_collision = False

    if len(liste_items) > 1 :

        for x in liste_items :

            if x != pacman_1 :

                test_collision = True

                break

    if test_collision == True :

        monCanvas.itemconfig(pacman_1, fill="red")

    else:

        monCanvas.itemconfig(pacman_1, fill="yellow")

    if liste_coord[2]>500 :

        vit_x = -10

    elif liste_coord[0]<0 :

        vit_x = 10

    elif liste_coord[1]<0 :

        vit_y = 10

    elif liste_coord[3]>600 :

        vit_y = -10

    if (vit_x <0 or vit_y>0) :

        mod_angle = 180

    if vit_y == 0 :

        if (monCanvas.itemcget(pacman_1, 'start') == '15.0' or monCanvas.itemcget(pacman_1, 'start') == '195.0') :

            monCanvas.itemconfig(pacman_1, start=30+mod_angle, extent=300)

        else:

            monCanvas.itemconfig(pacman_1, start=15+mod_angle, extent=330)

    if vit_x ==0 :

        if (monCanvas.itemcget(pacman_1, 'start') == '105.0' or monCanvas.itemcget(pacman_1, 'start') == '285.0') :

            monCanvas.itemconfig(pacman_1, start=120+mod_angle, extent=300)

        else:

            monCanvas.itemconfig(pacman_1, start=105+mod_angle, extent=330)

    monCanvas.move(pacman_1,vit_x,vit_y)

    modification2()

    if stop_animation == False :

        fen_princ.after(100, modification)

    else:

        stop_animation = False

        animation_active = False


def init_couleurs():

    but_avance.config(bg="black")

    but_recule.config(bg="black")

    but_monte.config(bg="black")

    but_descend.config(bg="black")

    but_init.config(bg="red")

    but_arret.config(bg="red")


def avance_x():

    print(but_avance.cget('bg'))

    init_couleurs()

    but_avance.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 10

    vit_y = 0

    if animation_active == False :

        modification()


def recule_x():

    init_couleurs()

    but_recule.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = -10

    vit_y = 0

    if animation_active == False :

        modification()


def monte_y():

    init_couleurs()

    but_monte.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 0

    vit_y = -10

    if animation_active == False :

        modification()


def descend_y():

    init_couleurs()

    but_descend.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 0

    vit_y = 10

    if animation_active == False :

        modification()


def point_depart():

    init_couleurs()

    but_init.config(bg="blue")

    global vit_x

    global vit_y

    vit_x = 0

    vit_y = 0

    arret()

    monCanvas.coords(pacman_1,50,50,150,150)

    monCanvas.itemconfig(pacman_1, start=15,extent=330)

    monCanvas.coords(pacman_2,350,350,450,450)

    monCanvas.itemconfig(pacman_2, start=15,extent=330)


def arret():

    init_couleurs()

    but_arret.config(bg="blue")

    global stop_animation

    stop_animation = True


def modification2():

    global vit_x2

    global vit_y2

    if animation_active == True :

        direction = random.randint(1,100)

        if direction > 80 :

            if direction > 95 :

                vit_x2 = 10

                vit_y2 = 0

            elif direction > 90 :

                vit_x2 = -10

                vit_y2 = 0

            elif direction > 85 :

                vit_x2 = 0

                vit_y2 = 10

            else:

                vit_x2 = 0

                vit_y2 = -10

        mod_angle = 0

        liste_coord = monCanvas.coords(pacman_2)

        if liste_coord[2]>500 :

            vit_x2 = -10

        elif liste_coord[0]<0 :

            vit_x2 =10

        elif liste_coord[1]<0 :

            vit_y2 = 10

        elif liste_coord[3]>600 :

            vit_y2 = -10

        if (vit_x2 <0 or vit_y2>0) :

            mod_angle = 180

        if vit_y2 == 0 :

            if (monCanvas.itemcget(pacman_2, 'start') == '15.0' or monCanvas.itemcget(pacman_2, 'start') == '195.0') :

                monCanvas.itemconfig(pacman_2, start=30+mod_angle, extent=300)

            else:

                monCanvas.itemconfig(pacman_2, start=15+mod_angle, extent=330)

        if vit_x2 ==0 :

            if (monCanvas.itemcget(pacman_2, 'start') == '105.0' or monCanvas.itemcget(pacman_2, 'start') == '285.0') :

                monCanvas.itemconfig(pacman_2, start=120+mod_angle, extent=300)

            else:

                monCanvas.itemconfig(pacman_2, start=105+mod_angle, extent=330)

        monCanvas.move(pacman_2,vit_x2,vit_y2)


# ----------------------------------------------------------------

# Corps du programme

# ----------------------------------------------------------------

fen_princ = Tk()

fen_princ.title("ESSAI AVEC CANVAS")

fen_princ.geometry("600x600")


monCanvas = Canvas(fen_princ, width=500, height=600, bg='ivory', bd=0, highlightthickness=0)

monCanvas.grid(row=0,column=0, padx=10,pady=10)

pacman_1 = monCanvas.create_arc(50,50,150,150,fill="yellow",start=15,extent=330)

pacman_2 = monCanvas.create_arc(350,350,450,450,fill="orange",start=15,extent=330)


zone2 = Frame(fen_princ, bg='#777777')

zone2.grid(row=0,column=1,ipadx=5)


but_avance = Button(zone2, text="Droite", fg="yellow", bg="black", command=avance_x)

but_recule = Button(zone2, text="Gauche", fg="yellow", bg="black", command=recule_x)

but_monte = Button(zone2, text="Monte", fg="yellow", bg="black", command=monte_y)

but_descend = Button(zone2, text="Descend", fg="yellow", bg="black", command=descend_y)

but_arret = Button(zone2, text="STOP", fg="yellow", bg="red", command=arret)

but_init = Button(zone2, text="INIT", fg="yellow", bg="red", command=point_depart)

but_avance.pack(fill=X)

but_recule.pack(fill=X)

but_monte.pack(fill=X)

but_descend.pack(fill=X)

but_arret.pack(fill=X)

but_init.pack(fill=X)


fen_princ.mainloop()