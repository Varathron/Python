from Tkinter import *


def doNothing():
    print("ok  ok")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

subMenu2 = Menu(menu)
menu.add_cascade(label="Edit", menu=subMenu2)
subMenu.add_command(label="Undo", command=doNothing)




root.mainloop()
