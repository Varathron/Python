# from Tkinter import *
import Tkinter as tk
import ttk 
import factors


def dictionary_finder(from_unit):
	if from_unit in factors.distance_dict_list:
		working_dict = factors.distance_dict_list[from_unit]
	elif from_unit in factors.temp_dict_list:
		working_dict = factors.temp_dict_list[from_unit]

	return working_dict

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

def input_getter():
	input_value = input_field.get()
	if len(input_value) == 0:
		return 0
	else:
		input_value = float(input_value)
		return input_value


def converter(input_value, from_unit, to_unit):
	result = 0
	if from_unit in factors.temps_labels:
		result = temp_converter(input_value, from_unit, to_unit)
	else:
		working_dict = dictionary_finder(from_unit)
		if to_unit in working_dict:
			factor = working_dict[to_unit]

		result = input_value * factor

	output.configure(text=str(result))


window = tk.Tk()

# window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Conversion")

#unit types tabs confioguration
tabs = ttk.Notebook(window)
tabs.grid(sticky='w')

distance_tab_frame = tk.Frame(tabs)
tabs.add(distance_tab_frame, text="Distance")

temp_tab_frame = tk.Frame(tabs)
tabs.add(temp_tab_frame, text="Temperature")

#variables
from_unit = tk.StringVar()
to_unit = tk.StringVar()

#distance section comboboxes--------------------
unit_selection_from = ttk.Combobox(distance_tab_frame, values=factors.distances_labels, textvariable=from_unit)
unit_selection_from.grid(row=0, column=0)

to_label = tk.Label(distance_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = ttk.Combobox(distance_tab_frame, values=factors.distances_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#END

#temp section comboboxes-------------------
unit_selection_from = ttk.Combobox(temp_tab_frame, values=factors.temps_labels, textvariable=from_unit)
unit_selection_from.grid(row=0, column=0)

to_label = tk.Label(temp_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = ttk.Combobox(temp_tab_frame, values=factors.temps_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#END


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
