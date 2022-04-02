from tkinter import *
from PIL import ImageTk, Image
import click

root = Tk()
root.title("DropDown")
root.geometry("500x500")

clicked = StringVar()
clicked.set("Monday")
options = ["Monday", 
"Tuesday", "Wedneday", "Thursday", "Friday"]

dropdown = OptionMenu(root, clicked, *options)
dropdown.pack()

root.mainloop()