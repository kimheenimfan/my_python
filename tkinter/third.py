#! /usr/bin/env python3

import tkinter as tk

root = tk.Tk()
tk.Label(root,text=" Enter your Password:").pack()
tk.Button(root,text="Search").pack()
tk.Checkbutton(root,text="RememberMe",value=True).pack()
tk.Entry(root,width=30).pack()
tk.Radiobutton(root,text="Male",value=1).pack()
tk.Radiobutton(root,text="Female",value=2).pack()
tk.OptionMenu(root,var,"Select Country","USA","UK","India","Others").pack()
tk.Scrollbar(root,orient=VERTICAL,command=mytext.yview).pack()
root.mainloop()
