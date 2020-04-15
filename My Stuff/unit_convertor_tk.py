from Tkinter import *

def input_getter():
    entry = float(input.get())
    return entry

def mph_to_kmh():
    input = input_getter()
    result = input * 1.60934
    output.configure(text=str(result))




window = Tk()

window.title("Unit Conversion")

b_distance = Button(window, text="MPH -> Km/H", command=mph_to_kmh)
b_distance.grid(row=0, column=0)

input = Entry(window, font=(20))
input.grid(row=1, column=0)

output = Label(window, text="OUTPUT", font=("Courier New Bold", 16))
output.grid(row=2, column=0)

window.mainloop()
