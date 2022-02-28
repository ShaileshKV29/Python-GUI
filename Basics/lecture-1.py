from cProfile import label
from tkinter import *

from matplotlib.pyplot import title

root = Tk()

myLabel = Label(root, text="Hello World!")
myLabel.pack()

root.mainloop()