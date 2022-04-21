from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from setuptools import Command
root = Tk()
root.title("Data Generator")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
#mainframe = ttk.Frame(root, padding = "3 3 3 3")
frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
#frame = ttk.Frame(mainframe, borderwidth=0, relief="ridge")

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.geometry("500x350")

def submit():
    data_gen_mk2()

#creating a label widget
#myLabel1 = Label(root, text = "Welcome to the Data Generating tool!")
#myLabel2 = Label(root, text = "Where is your store located?")

#shoving it onto the screen
#myLabel.pack()
#myLabel1.grid(column = 0, row = 0) #welcome
#myLabel2.grid(column = 0, row = 1) #zipcode

#yLabel2.grid(row = 1, column = 0)
ttk.Label(mainframe, text="Welcome to the Data Generating tool!").place(anchor = CENTER, relx = .5, rely = .05)
#ttk.Label(mainframe, text="Welcome to the Data Generating tool!", justify='center').grid(column=0, row=0)
ttk.Label(mainframe, text="Where is your store located?").grid(column=0, row=1)
ttk.Entry(mainframe, text="ZIPCODE").grid(column=1, row=1)
ttk.Button(mainframe, text="Generate", command=submit).grid(column=1, row=2)
ttk.Label(mainframe, text="Run the program to generate data.").grid(column=0, row=2)

#root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#mainframe.columnconfigure(0, weight=1)
#mainframe.columnconfigure(1, weight=1)
#mainframe.columnconfigure(2, weight=1)
#mainframe.columnconfigure(3, weight=1)
#mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(1, weight=1)
root.mainloop()