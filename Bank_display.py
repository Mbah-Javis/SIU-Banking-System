from tkinter import*
import os
from PIL import ImageTk, Image

#main Screen menu
master = Tk()
master.title("banking app")
#img import
img=Image.open('Banking.png')
img=img.resize((150,150))
img.show()
img=ImageTk.PhotoImage(img)