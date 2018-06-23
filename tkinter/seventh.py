#! /usr/bin/env python3
import tkinter as tk
root = tk.Tk()
root.title("Find & Replace")
tk.Label(root,text="Find:").grid(row=0,column=0,sticky=tk.E)
tk.Entry(root,width=60).grid(row=0,column=1,padx=2,pady=2,sticky=tk.W+tk.E,columnspan=9)
tk.Label(root,text="Replace:").grid(row=1,column=0,sticky=tk.E)
tk.Entry(root).grid(row=1,column=1,sticky=tk.W+tk.E,padx=2,pady=2,columnspan=9)
tk.Button(root,text="Find").grid(row=0,column=10,sticky=tk.W+tk.E,padx=2)
tk.Button(root,text="Find All").grid(row=1,column=10,sticky=tk.W+tk.E,padx=2)
tk.Button(root,text="Replace").grid(row=2,column=10,sticky=tk.W+tk.E,padx=2)
tk.Button(root,text="Replace All").grid(row=3,column=10,sticky=tk.W+tk.E,padx=2)
root.mainloop()

