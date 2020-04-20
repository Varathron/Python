from Tkinter import *
from ttk import *
import factors


class UnitConverter:

	def __init__(self, main):
		window.resizable(False, False)
		window.title("Unit Conversion")

		self.tabs = Notebook(main)
		self.tabs.grid(sticky='w')

		self.distance_tab_frame = Frame(self.tabs)
		self.tabs.add(self.distance_tab_frame, text="Distance")

		self.temp_tab_frame = Frame(self.tabs)
		self.tabs.add(self.temp_tab_frame, text="Temperature")

		#comboboxes variables
		self.from_unit = StringVar()
		self.to_unit = StringVar()

		#distance section comboboxes--------------------
		self.unit_selection_from = Combobox(self.distance_tab_frame, values=factors.distances_labels, textvariable=self.from_unit)
		self.unit_selection_from.grid(row=0, column=0)

		self.to_label = Label(self.distance_tab_frame, text=" to ")
		self.to_label.grid(row=0, column=1)

		self.unit_selection_from = Combobox(self.distance_tab_frame, values=factors.distances_labels, textvariable=self.to_unit)
		self.unit_selection_from.grid(row=0, column=2)
		#END

		#temp section comboboxes-------------------
		self.unit_selection_from = Combobox(self.temp_tab_frame, values=factors.temps_labels, textvariable=self.from_unit)
		self.unit_selection_from.grid()

		self.to_label = Label(self.temp_tab_frame, text=" to ")
		self.to_label.grid(row=0, column=1)

		self.unit_selection_from = Combobox(self.temp_tab_frame, values=factors.temps_labels, textvariable=self.to_unit)
		self.unit_selection_from.grid(row=0, column=2)
		#END


		self.middle_frame = Frame(main, padding=10)
		self.middle_frame.grid(row=1)

		self.input_field = Entry(self.middle_frame, font=(20))
		self.input_field.grid()

		self.convert_button = Button(self.middle_frame, text="Convert", command=lambda: self.converter(self.input_getter(), self.from_unit.get(), self.to_unit.get()))
		self.convert_button.grid(row=1)

		self.lower_text_frame = LabelFrame(main, text="Result")
		self.lower_text_frame.grid(row=2)

		self.output = Label(self.lower_text_frame, font=(20), width=14)
		self.output.grid()


	def output_set(self, output_value):
		self.output.configure(text=str(self.output_value))

	def input_getter(self):
		self.input_value = self.input_field.get()
		if len(self.input_value) == 0:
			return 0
		else:
			self.input_value = float(self.input_value)
			return self.input_value

	def temp_converter(self, input_value, from_unit, to_unit):
		if self.from_unit == "Celsius":
			if self.to_unit == "Kelvin":
				self.result = self.input_value + 273.15
			elif self.to_unit == "Fahrenheit":
				self.result = (self.input_value * 9/5) + 32
			elif self.to_unit == "Celsius":
				self.result = self.input_value
		elif self.from_unit == "Kelvin":
			if self.to_unit == "Celsius":
				self.result = self.input_value - 273.15
			elif self.to_unit == " Fahrenheit":
				self.result = (self.input_value - 273.15) * 9/5 + 32
			elif self.to_unit == "Kelvin":
				self.result = self.input_value
		elif self.from_unit == "Fahrenheit":
			if self.to_unit == "Celsius":
				self.result = (self.input_value - 32) * 5/9
			elif self.to_unit == "Kelvin":
				self.result = (self.input_value - 32) * 5/9 + 273.15
			elif self.to_unit == "Fahrenheit":
				self.result = self.input_value

		return self.result

	#using 2D list	
	def converter(self, input_value, from_unit, to_unit):
		if self.from_unit in factors.temps_labels:
			self.result = self.temp_converter(self.input_value, self.from_unit, self.to_unit)
		else:
			if self.from_unit in factors.distance_grid_index:
				self.row = factors.distance_grid_index[self.from_unit]
				if self.to_unit in factors.distance_grid_index:
					self.column = factors.distance_grid_index[self.to_unit]

			self.factor = factors.distance_grid[row][self.column]
			self.result = self.input_value * self.factor

		output_set(self.result)




window = Tk()

main_program = UnitConverter(window)

window.mainloop()