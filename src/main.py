import random
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import book

gBooks = [];

gBooks.append(book.Book())

#Window Setup
root = ttk.Window(themename='journal')
root.title("BookWormPy")
root.geometry('1280x920')

#Top menu bar
menuBar = ttk.Menu(master = root)
filemenu = ttk.Menu(menuBar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=filemenu)

helpmenu = ttk.Menu(menuBar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menuBar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menuBar)

#Side menu

#Run app
root.mainloop()