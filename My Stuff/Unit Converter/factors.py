#temps------------------
temps_labels = ["Kelvin", "Celsius", "Fahrenheit"]

#]---------------DISTANCES---------------------------------------[
#order of display of units in the comboboxes
distances_labels = [
	"Kilometer", 
	"Meter", 
	"Centimeter", 
	"Millimeter", 
	"Mile", 
	"Yard", 
	"Foot", 
	"Inch"
]

#index dict for finding correct row and column in converter function
distance_grid_index = {
	'Kilometer' : 0,
	'Mile' : 4, 
	'Yard' : 5,
	'Foot' : 6,
	'Inch' : 7,
	'Meter' : 1,
	'Centimeter' : 2,
	'Millimeter' : 3
}

#distance unit factors grid 
#	Kilometer 	Meter       Centimeter  Millimeter      Mile            Yard            Foot            Inch
distance_grid = [
	[1, 		1000, 		100000, 	1000000, 		0.6213688756, 	1093.6132983, 	3280.839895, 	39370.07874], 	#Kilometer
	[0.001, 	1, 			100, 		1000,			0.0006213689, 	1.0936132983, 	3.280839895, 	39.37007874],	#Meter
	[0.00001,	0.01, 		1, 			10, 			0.0000062137, 	0.010936133, 	0.0328083990, 	0.3937007874],	#Centimeter
	[0.000001, 	0.001, 		0.1, 		1, 				0.0000062137, 	0.0010936133, 	0.0032808399, 	0.0393700787],	#Millimeter
	[1.60935, 	1609.35, 	160935, 	1609350, 		1,				1760.0065617, 	5280.019685, 	63360.23622],	#Mile
	[0.0009144, 0.9144, 	91.44, 		914.4, 			0.0005681797, 	1, 				3, 				36],			#Yard
	[0.0003048, 0.3048, 	30.48, 		304.8, 			0.0001893932, 	0.3333333333, 	1, 				12],			#Foot
	[0.0000254, 0.0254, 	2.54, 		25.4, 			0.0000157828, 	0.0277777778, 	0.0833333333, 	1] 				#Inch
]
#-----------------------END DISTANCES SECTION----------------------------------

#--------------------------SPEEDS---------------------------------------------