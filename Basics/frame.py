from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.geometry("400x300")
root.iconbitmap('Basics/icon.ico')

frame = LabelFrame(root, text="May be A Div Tag?", padx=35, pady=25, border=0)
frame.pack(padx=10, pady=10)

btn = Button(frame, text="Exit Program", command=root.quit)
btn.pack()

exit_btn = Button(root, text="Exit Program", command=root.quit)
exit_btn.pack()

root.mainloop()