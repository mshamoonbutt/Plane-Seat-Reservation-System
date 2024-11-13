from tkinter import *
import math
import random

root = Tk()
root.title("Root Window")
root.geometry('350x200')

def BtnClick(e=None):
    str = lbl["text"]
    lbl.configure(text = "[ " + str + " ]")
btn = Button(root, text = "Click me", command=BtnClick)
btn.grid(column=0, row=0)
btn.bind("<Button-3>",BtnClick)
    
child = Tk()
child.title("Child Window")
child.geometry('200x350')

def LblClick(e):
    print("Child label clicked...")
lbl = Label(child, text = "Waiting...")
lbl.grid(column=0, row=0)
#lbl.bind("<Button-1>",LblClick)
#lbl.bind("<Button-3>",LblClick)


root.mainloop()
