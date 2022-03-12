from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("PopUp")

# Different Types of Message Boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is Title", "This is Text")
    Label(root, text=response).pack()

Button(root, text="Click", command=popup).pack()

root.mainloop()
