from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")
myGridLabel = Label(root, text="Grid System")

myLabel.grid(row=10, column=0)
myGridLabel.grid(row=1, column=0)

root.mainloop()