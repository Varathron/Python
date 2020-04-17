from Tkinter import *
# import Tkinter as tk
from ttk import *
# import ttk 
import factors


def output_set(output_value):
	output.configure(text=str(output_value))


def input_getter():
	input_value = input_field.get()
	if len(input_value) == 0:
		return 0
	else:
		input_value = float(input_value)
		return input_value


def temp_converter(input_value, from_unit, to_unit):
	if from_unit == "Celsius":
		if to_unit == "Kelvin":
			result = input_value + 273.15
		elif to_unit == "Fahrenheit":
			result = (input_value * 9/5) + 32
		elif to_unit == "Celsius":
			result = input_value
	elif from_unit == "Kelvin":
		if to_unit == "Celsius":
			result = input_value - 273.15
		elif to_unit == " Fahrenheit":
			result = (input_value - 273.15) * 9/5 + 32
		elif to_unit == "Kelvin":
			result = input_value
	elif from_unit == "Fahrenheit":
		if to_unit == "Celsius":
			result = (input_value - 32) * 5/9
		elif to_unit == "Kelvin":
			result = (input_value - 32) * 5/9 + 273.15
		elif to_unit == "Fahrenheit":
			result = input_value

	return result


#using 2D list	
def converter(input_value, from_unit, to_unit):
	if from_unit in factors.temps_labels:
		result = temp_converter(input_value, from_unit, to_unit)
	else:
		if from_unit in factors.distance_grid_index:
			row = factors.distance_grid_index[from_unit]
			if to_unit in factors.distance_grid_index:
				column = factors.distance_grid_index[to_unit]

		factor = factors.distance_grid[row][column]
		result = input_value * factor

	output_set(result)


window = Tk()

# window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Conversion")

#unit types tabs configuration
tabs = Notebook(window)
tabs.grid(sticky='w')

distance_tab_frame = Frame(tabs)
tabs.add(distance_tab_frame, text="Distance")

temp_tab_frame = Frame(tabs)
tabs.add(temp_tab_frame, text="Temperature")

#comboboxes variables
from_unit = StringVar()
to_unit = StringVar()

#distance section comboboxes--------------------
unit_selection_from = Combobox(distance_tab_frame, values=factors.distances_labels, textvariable=from_unit)
unit_selection_from.grid(row=0, column=0)

to_label = Label(distance_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = Combobox(distance_tab_frame, values=factors.distances_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#END

#temp section comboboxes-------------------
unit_selection_from = Combobox(temp_tab_frame, values=factors.temps_labels, textvariable=from_unit)
unit_selection_from.grid()

to_label = Label(temp_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = Combobox(temp_tab_frame, values=factors.temps_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#END


middle_frame = Frame(window, padding=10)
middle_frame.grid(row=1)

input_field = Entry(middle_frame, font=(20))
input_field.grid()

convert_button = Button(middle_frame, text="Convert", command=lambda: converter(input_getter(), from_unit.get(), to_unit.get()))
convert_button.grid(row=1)

lower_text_frame = LabelFrame(window, text="Result")
lower_text_frame.grid(row=2)

output = Label(lower_text_frame, font=(20), width=14)
output.grid()

window.mainloop()
