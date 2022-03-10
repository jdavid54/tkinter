from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
#root.iconbitmap('/home/pi/')

my_img = ImageTk.PhotoImage(Image.open('/home/pi/Pictures/on the fly.jpg'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()