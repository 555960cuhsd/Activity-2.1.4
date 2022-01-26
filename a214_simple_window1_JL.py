#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
from ast import arguments
from distutils import command
import tkinter as tk

def test_my_button():
  frame_auth.tkraise()
  frame_lbl = tk.Label(frame_auth, text = ent_password.get(), font = "Times")
  frame_lbl.pack()

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authorization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

# Username
lbl_username = tk.Label(frame_login, text='Username:', font = "Times")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

# Password
lbl_password = tk.Label(frame_login, text = "Password:", font = "Times")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)

# Button
btn_login = tk.Button(frame_login, bd=3, text="Login", command=test_my_button)
btn_login.pack(pady=5)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

frame_login.tkraise()
root.mainloop()