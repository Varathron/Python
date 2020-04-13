from Tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn Tkinter')

frame = LabelFrame(root, padx=55, pady=55)
frame.pack(padx=100, pady=100)

b = Button(frame, text='Dont click here!')
b2 = Button(frame, text='Dont click here!')
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
