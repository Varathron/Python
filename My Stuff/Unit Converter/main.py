# from Tkinter import *
import Tkinter as tk
import ttk 

distances_units = {
	"kilometer_2_mile" : 0.6213688756,
	"mile_2_kilometer" : 1.60935
}

distances_labels = ["Kilometer", "Mile"]


def input_getter():
	entry = input_field.get()
	if len(entry) == 0:
		return 0
	else:
		entry = float(entry)
		return entry


def converter(input_value, from_unit, to_unit):
	factor = 0

	if from_unit == 'Kilometer':
		if to_unit == 'Mile':
			factor = distances_units["kilometer_2_mile"]
		else:
			factor = 1
	else:
		if to_unit == 'Kilometer':
			factor = distances_units["mile_2_kilometer"]
		else:
			factor = 1

	result = input_value * factor
	output.configure(text=str(result))


window = tk.Tk()

window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Conversion")


tabs = ttk.Notebook(window)
tabs.grid(sticky='w')


distance_tab_frame = tk.Frame(tabs)
tabs.add(distance_tab_frame, text="Distance")

speed_tab_frame = tk.Frame(tabs)
tabs.add(speed_tab_frame, text="Speed")


from_unit = tk.StringVar()
to_unit = tk.StringVar()

unit_selection_from = tk.OptionMenu(distance_tab_frame, from_unit, *distances_labels)
unit_selection_from.grid(row=0, column=0)

to_label = tk.Label(distance_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_to = tk.OptionMenu(distance_tab_frame, to_unit, *distances_labels)
unit_selection_to.grid(row=0, column=2)


middle_frame = tk.Frame(window, bd=10)
middle_frame.grid(row=1)

convert_button = tk.Button(middle_frame, text="Convert", pady=10, padx=20, command=lambda: converter(input_getter(), from_unit.get(), to_unit.get()))
convert_button.grid(row=1)


lower_frame = tk.Frame(window, bd=10)
lower_frame.grid(row=2)


input_field = tk.Entry(middle_frame, font=(20))
input_field.grid(row=0, column=0)

output = tk.Label(lower_frame, text="OUTPUT", font=(20), anchor='w', bd=6, relief="ridge", width=12)
output.grid(row=2, column=0)

window.mainloop()
