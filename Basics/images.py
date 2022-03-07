from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.geometry("400x300")
root.iconbitmap('Basics/icon.ico')

img = ImageTk.PhotoImage(Image.open("Basics/Gojo.jfif"))
lbl = Label(root, image=img)
lbl.pack()



exit_btn = Button(root, text="Exit Program", command=root.quit)
exit_btn.pack()

root.mainloop()