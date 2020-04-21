from Tkinter import *
from ttk import *
import random

pool = []
# pool = ["A", "B", "c", "d", "e", "f", "g", "h", "j", "k", "A", "B", "c", "d", "e", "f", "g", "h", "j", "k",]
picked = []
brands = ['Mercedes', 'Ferrari', 'Red Bull', 'Renault', 'Haas', 'McLaren', 'Racing Point', 'Toro Rosso', 'Alfa Romeo', 'Williams']
brandstxt =''

def submit_to_list():
	name = entry.get()
	pool.append(name)
	entry.delete(0, "end")

def pick_teams():

	textvar = ''
	
	for i in range(len(pool)):
		picked_name = random.choice(pool)
		picked.append(picked_name)
		pool.remove(picked_name)
		
		
	for i in range(len(picked)):

		if (i % 2 ==0):
			textvar += "\n"
			textvar += picked[i-1]
			
		else:
			textvar +=" + "
			textvar += picked[i-1]


		names_label.configure(text=textvar)
		

main = Tk()
main.title("Groups")

main_frame = Frame(main)
main_frame.pack()

input_name = StringVar()
entry = Entry(main_frame, textvariable=input_name)
entry.grid(row=0, column=0)

submit_button = Button(main_frame, text='Submit', command=submit_to_list)
submit_button.grid(row=0, column=1)

pick_pairs_button = Button(main_frame, text='Pick Teams', command=pick_teams)
pick_pairs_button.grid(row=1, column=0)

teams_label = Label(main_frame)
teams_label.grid(row=2)

names_label = Label(main_frame)
names_label.grid(row=2, column=1)

for i in range(len(brands)):

		brandstxt += "\n"
		brandstxt += brands[0]
		del brands[0]

		teams_label.configure(text=brandstxt)	

main.mainloop()