from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

class MyWindow:
    def __init__(self):
        self._window = Tk()
        self._window.title("My Window")
        self._window.geometry('500x150+50+400')
        self._window.configure(background='black')
        
        self.CreateLayout()
        
    def CreateLayout(self):
        lbl = Label(self._window, text = "Hey there")
        lbl.grid(column=0, row = 0)
        
        btn = Button(self._window, text = "click Me", bg="green", fg="red", state=DISABLED)
        btn.grid(column=0, row=1)
        
        btn = Button(self._window, text = "click Me again", bg="#00ff99", fg="red", command=self.ClickMeAgain)
        btn.grid(column=0, row=2)
        
        btn = Button(self._window, text = "Load", bg="orange", fg="red", command=self.LoadFile)
        btn.grid(column=0, row=3)
        
        btn = Button(self._window, text = "Save", bg="orange", fg="red", command=self.SaveFile)
        btn.grid(column=0, row=4)


    def ClickMeAgain(self):
        messagebox.showinfo("Info", "Button clicked")
        print("print message on the console too")
        
    def LoadFile(self):
        fname = askopenfilename(filetypes=(("Project 1 files", "*.txt"),
                                           ("All files", "*.*") ))
        print(fname)
        file = open(fname, "r")
        print(file.read())
        file.close()
        
    def SaveFile(self):
        fname = asksaveasfile(mode='w+', defaultextension=".txt")
        if fname is None:
            return
        text2save = str("this is a miracle")
        fname.write(text2save)
        fname.close()
        
        
