from tkinter import *

from pyparsing import col

root = Tk()

def myClick():
    mylabel = Label(root, text="Button Clicked!")
    mylabel.pack()

btn = Button(root, text="Button", borderwidth=1, padx=30, pady=5, command=myClick)
btn.pack()

root.mainloop()