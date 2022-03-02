from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.geometry("400x300")
root.iconbitmap('Basics/icon.ico')

frame = LabelFrame(root, text="May be A Div Tag?", padx=5, pady=5)
frame.pack(padx=10, pady=10)

exit_btn = Button(root, text="Exit Program", command=root.quit)
exit_btn.pack()

root.mainloop()