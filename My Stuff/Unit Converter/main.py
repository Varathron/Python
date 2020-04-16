# from Tkinter import *
import Tkinter as tk
import ttk 
import factors


speed_labels = ['TEST']
distance_labels = list(factors.kilometer.keys())

distance_dict_list = {
	'Kilometer' : factors.kilometer,
	'Mile' : factors.mile, 
	'Yard' : factors.yard,
	'Foot' : factors.foot,
	'Inch' : factors.inch,
	'Meter' : factors.meter,
	'Centimeter' : factors.centimeter,
	'Millimiter' : factors.millimeter
	}


def dictionary_finder(from_unit):

	if from_unit in distance_dict_list:
		working_dict = distance_dict_list[from_unit]
	elif from_unit in speed_dict_list:
		working_dict = speed_dict_list[from_unit]



	return working_dict


def input_getter():
	input_value = input_field.get()
	if len(input_value) == 0:
		return 0
	else:
		input_value = float(input_value)
		return input_value


def converter(input_value, from_unit, to_unit):
	factor = 0
	
	working_dict = dictionary_finder(from_unit)

	if to_unit in working_dict:
		factor = working_dict[to_unit]
	
	result = input_value * factor
	output.configure(text=str(result))



window = tk.Tk()

# window.geometry("600x400")
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

#distance section
unit_selection_from = ttk.Combobox(distance_tab_frame, values=distance_labels, textvariable=from_unit)
unit_selection_from.grid(row=0, column=0)

to_label = tk.Label(distance_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = ttk.Combobox(distance_tab_frame, values=distance_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#end of distance section

#speed section
unit_selection_from = ttk.Combobox(speed_tab_frame, values=speed_labels, textvariable=from_unit)
unit_selection_from.grid(row=0, column=0)

to_label = tk.Label(speed_tab_frame, text=" to ")
to_label.grid(row=0, column=1)

unit_selection_from = ttk.Combobox(speed_tab_frame, values=speed_labels, textvariable=to_unit)
unit_selection_from.grid(row=0, column=2)
#end of speed section










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
