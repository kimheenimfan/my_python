#! /usr/bin/env python3
import tkinter as tk
root = tk.Tk()
my_label = tk.Label(root,text="I am a label widget")
my_button = tk.Button(root,text="I am a button widget")
my_label.pack()
my_button.pack()
root.mainloop()

