from ast import arguments
from distutils import command
import tkinter as tk
root = tk.Tk()
root.wm_geometry("450x400")
root.title("tk")

f1 = tk.Frame(root, bg = "blue", height=200, width=300)
f1.grid(row = 1, column = 1, sticky="news")


f2 = tk.Frame(root, bg = "red", height=200, width=300)
f2.grid(row = 2, column = 1, sticky="news")


f3 = tk.Frame(root, bg = "lime", height=200, width=150)
f3.grid(row = 1, column = 2, sticky="news")


f4 = tk.Frame(root, bg = "yellow", height=200, width=150)
f4.grid(row = 2, column = 2, sticky="news")


root.mainloop()