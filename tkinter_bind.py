from tkinter import *

def f(event):
    t=event.keysym
    print("Touche pressée :", t)

def g(event):
    x=event.x
    y=event.y
    print("Position :", x, y)

root = Tk()

root.bind("<Key>", f)
root.bind("<Motion>",g)
root.mainloop()