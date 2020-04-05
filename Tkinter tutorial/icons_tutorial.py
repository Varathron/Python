from Tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Tkinter icons tutorial')
root.iconbitmap('middle.ico')

my_img = ImageTk.PhotoImage(Image.open("middle.ico"))
my_label = Label(image=my_img)
my_label.pack()













button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
