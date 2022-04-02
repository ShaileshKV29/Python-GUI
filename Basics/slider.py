from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("File Dialog")

vertical = Scale(root, from_=200, to=1000)
vertical.pack()

horizontal = Scale(root, from_=200, to=1000, orient=HORIZONTAL)
horizontal.pack()

def resize():
    root.geometry(f"{horizontal.get()}x{vertical.get()}")

resize_btn = Button(root, text="Resize Window", command=resize).pack()

root.mainloop()