from tkinter import *

root = Tk()
root.geometry("400x300")
input_box = Entry(root)
input_box.pack()

def displayName():
    name = Label(root, text=f"{input_box.get()}")
    name.pack()
    input_box.delete(0, END)

btn = Button(root, text="Enter Name", command=displayName)
btn.pack()

root.mainloop()