from Tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tkinter icons tutorial')
#root.iconbitmap('middle.ico') doesnt work on linux

my_img1 = ImageTk.PhotoImage(Image.open("a.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("b.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("c.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("d.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("e.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

image_number = 1
status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=my_img1)
my_label.grid(row=1, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == (len(image_list)):
        button_forward = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=2)

    #update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == (1):
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=2)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=0, column=0, sticky=W+E)
button_exit.grid(row=0, column=1, sticky=W+E)
button_forward.grid(row=0, column=2, sticky=W+E)




root.mainloop()
