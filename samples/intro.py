from tkinter import *
from mywindow import *

root = Tk()
root.title("Root Window")
root.geometry('350x200')

lbl = Label(root, text = "Hello COMP 111")
lbl.grid(column=0, row = 0)
lbl = Label(root, text = "Another Label")
lbl.grid(column=0, row = 1)
lbl = Label(root, text = "Big Label")
lbl.place(x=100, y=80)
lbl = Label(root, text = "Cool Label", fg="red", bg = "#99ff33", font=("Arial Bold", 40))
lbl.place(x=10, y=110)


window2 = Tk()
window2.title("Slave Window")
window2.geometry('200x350+450+20')

lbl = Label(window2, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window2,width=10)
txt.grid(column=0, row=1)
def clicked():
    msg = txt.get()
    lbl.configure(text="--[ " + msg + " ]--")
    lb.insert(0, msg)
 
btn = Button(window2, text="Click Me", command=clicked)
btn.grid(column=0, row=2)

def LBClick(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    
#lb = Listbox(window2, command=LBClick)
lb = Listbox(window2)
lb.insert(0, "hello there")
lb.insert(0, "Ahmed")
lb.insert(0, "Ali")
lb.insert(0, "Zain")
lb.insert(0, "Coner")
lb.grid(column=0,row=3)
lb.bind('<<ListboxSelect>>', LBClick)


mywindow = MyWindow()



#---------------------------------
root.mainloop()
