from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Dialog")

def openFile():
    # This will return the address of the choosen file
    root.filename = filedialog.askopenfilename(initialdir='/', title="Select Files", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    myLabel2 = Label(root, text=root.filename).pack()

    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    myLabel = Label(image=my_img).pack()

btn = Button(root, text="Open File", command=openFile).pack()

root.mainloop()