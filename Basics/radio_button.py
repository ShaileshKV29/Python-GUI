from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.geometry("400x300")
root.iconbitmap('Basics/icon.ico')

r = IntVar()

Radiobutton(root, text="Option 1", variable=r, value=1)
Radiobutton(root, text="Option 2", variable=r, value=2)

btn = Button(root, text="Display Option", command=root.quit)
btn.pack()

exit_btn = Button(root, text="Exit Program", command=root.quit)
exit_btn.pack()

root.mainloop()