# from Tkinter import *
import Tkinter as tk
import ttk 

mph_to_kmh = 1.60935
kmh_to_mph = 0.6213688756



def input_getter():
	entry = input_field.get()
	if len(entry) == 0:
		return 0
	else:
		entry = float(entry)
	return entry


def converter(input_value, conversion):
    input_value = input_getter()
    result = input_value * conversion
    output.configure(text=str(result))


window = tk.Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Conversion")



tabs = ttk.Notebook(window)

speed_tab = tk.Frame(tabs)
tabs.add(speed_tab, text='Speed')
tabs.grid(row=0, column=0)

weights_tab = tk.Frame(tabs)
tabs.add(weights_tab, text='Weights')
tabs.grid(row=0, column=0)

middle_frame = tk.Frame(window, bd=10)
middle_frame.grid(row=1)

lower_frame = tk.Frame(window, bd=10)
lower_frame.grid(row=2)



mph2kmh = tk.Button(speed_tab, text="MPH to Km/H", command=lambda: converter(input_getter(), mph_to_kmh))
mph2kmh.grid(row=0, column=0, sticky='E')

kmh2mph = tk.Button(speed_tab, text="Km/h to MPH", command=lambda: converter(input_getter(), kmh_to_mph))
kmh2mph.grid(row=1, column=0)

mph2kts = tk.Button(speed_tab, text="MPH to KTS", )
mph2kts.grid(row=0, column=1)

kts2mph = tk.Button(speed_tab, text="KTS to MPH", )
















input_field = tk.Entry(middle_frame, font=(20))
input_field.grid(row=1, column=0)

output = tk.Label(lower_frame, text="OUTPUT", font=(20), anchor='w', bd=6, relief="ridge", width=12)
output.grid(row=2, column=0)

window.mainloop()
