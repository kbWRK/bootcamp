# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("500x500")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 225, y = 240)
top.mainloop()
