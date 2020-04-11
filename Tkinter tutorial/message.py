from Tkinter import *
from PIL import ImageTk,Image
import tkMessageBox

root = Tk()
root.title('Learn Tkinter')

def popup():
    response = tkMessageBox.askyesno("This is my popup", "Hello world")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="YES!").pack()
    # else:
    #     Label(root, text="NO").pack()


Button(root, text="Popup", command=popup).pack()









root.mainloop()
