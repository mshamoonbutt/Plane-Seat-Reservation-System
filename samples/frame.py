from tkinter import *
from mywindow import *

root = Tk()
root.title("Root Window")
root.geometry('350x200')

lbl = Label(root, text = "Hello COMP 111")
lbl.grid(column=0, row = 0)
lbl = Label(root, text = "Another Label")
lbl.grid(column=0, row = 1)

frame = Frame(root)
frame.grid(column=1, row = 1)
#frame1.place(x=60, y=70)

btn = Button(frame, text="B")
btn.grid(column=0, row=0)
btn = Button(frame, text="B")
btn.grid(column=1, row=0)
btn = Button(frame, text="B")
btn.grid(column=0, row=1)
btn = Button(frame, text="B")
btn.grid(column=1, row=1)



#---------------------------------
root.mainloop()
