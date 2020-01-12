#!/usr/bin/python3


import tkinter
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("1000x1000")

def HelloCallBack():
    msg = messagebox.showinfo("twoj pierwszy 'gui'", "Hello world")

B = Button(top, text = "hello", command = HelloCallBack)
B.place(x = 500, y = 500)
top.mainloop()