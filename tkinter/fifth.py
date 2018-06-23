#! /usr/bin/env python3
import tkinter as tk
root = tk.Tk()
parent = tk.Frame(root)
tk.Button(parent,text="ALL IS WELL").pack(fill=tk.X)
tk.Button(parent,text="BACK TO BASICS").pack(fill=tk.X)
tk.Button(parent,text="CATCH ME IF YOU CAN").pack(fill=tk.X)
tk.Button(parent,text="LEFT").pack(side=tk.LEFT)
tk.Button(parent,text="CENTER").pack(side=tk.LEFT)
tk.Button(parent,text="RIGHT").pack(side=tk.LEFT)
parent.pack(fill=tk.X)
root.mainloop()
