#distances-------------------------
distances_labels = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]


kilometer = {
	"Mile" : 0.6213688756,
	"Yard" : 1093.6132983,
	"Foot" : 3280.839895,
	"Inch" : 39370.07874,
	"Kilometer" : 1,
	"Meter" : 1000,
	"Centimeter" : 100000,
	"Millimeter" : 1000000
}

mile = {
	"Mile" : 1,
	"Yard" : 1760.0065617,
	"Foot" : 5280.019685,
	"Inch" : 63360.23622,
	"Kilometer" : 1.60935,
	"Meter" : 1609.35,
	"Centimeter" : 160935,
	"Millimeter" : 1609350
	
}

yard = {
	"Mile" : 0.0005681797,
	"Yard" : 1,
	"Foot" : 3,
	"Inch" : 36,
	"Kilometer" : 0.0009144,
	"Meter" : 0.9144,
	"Centimeter" : 91.44,
	"Millimeter" : 914.4
}

foot = {
	"Mile" : 0.0001893932,
	"Yard" : 0.3333333333,
	"Foot" : 1,
	"Inch" : 12,
	"Kilometer" : 0.0003048,
	"Meter" : 0.3048,
	"Centimeter" : 30.48,
	"Millimeter" : 304.8
}

inch = {
	"Mile" : 0.0000157828,
	"Yard" : 0.0277777778,
	"Foot" : 0.0833333333,
	"Inch" : 1,
	"Kilometer" : 0.0000254,
	"Meter" : 0.0254,
	"Centimeter" : 2.54,
	"Millimeter" : 25.4
}

meter = {
	"Mile" : 0.0006213689,
	"Yard" : 1.0936132983,
	"Foot" : 3.280839895,
	"Inch" : 39.37007874,
	"Kilometer" : 0.001,
	"Meter" : 1,
	"Centimeter" : 100,
	"Millimeter" : 1000
}

centimeter = {
	"Mile" : 0.0000062137,
	"Yard" : 0.010936133,
	"Foot" : 0.032808399,
	"Inch" : 0.3937007874,
	"Kilometer" : 0.00001,
	"Meter" : 0.01,
	"Centimeter" : 1,
	"Millimeter" : 10
}

millimeter = {
	"Mile" : 0.0000062137,
	"Yard" : 0.010936133,
	"Foot" : 0.032808399,
	"Inch" : 0.3937007874,
	"Kilometer" : 0.00001,
	"Meter" : 0.01,
	"Centimeter" : 1,
	"Millimeter" : 10
}
#END
distance_dict_list = {
	'Kilometer' : kilometer,
	'Mile' : mile, 
	'Yard' : yard,
	'Foot' : foot,
	'Inch' : inch,
	'Meter' : meter,
	'Centimeter' : centimeter,
	'Millimiter' : millimeter
}


#temps------------------
temps_labels = ["Kelvin", "Celsius", "Fahrenheit"]