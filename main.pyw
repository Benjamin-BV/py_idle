### MAKE A GAME DOC FOR IMPLEMENTATION ###

### OTHER FILES IMPORTS FOR FUNCTIONS ###



from tkinter import *
from tkinter import ttk

### BASIC TEST WINDOW ###

root = Tk()
frame = ttk.Frame(root, padding = 10)
frame.grid()
ttk.Label(frame, text="Hello World").grid(row=0,column=0)
ttk.Button(frame,text="Quit",command=root.destroy).grid(row=1,column=0)

### ADDING FUNCTION TO HAVE A RUNTIME TO INCREMENT ###













root.mainloop()
