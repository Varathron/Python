import Tkinter as tk

root = tk.Tk()

logo = tk.PhotoImage(file="python.gif")



explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root, justify = tk.LEFT, compound = tk.LEFT, padx=10,  text=explanation, image=logo).pack(side="right")
# w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation).pack(side="left")




root.mainloop()
