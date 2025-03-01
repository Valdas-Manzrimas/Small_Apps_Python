from cefpython3 import cefpython as cef
import os
import platform
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    print("PIP in not installed,"
    "Install it by typing 'pip install PIL' in the command prompt")
    sys.exit(1)




import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

class Widgets:
    def __init__(self, labtext, set_variable):
        self.lab = tk.Label(root, text=labtext)
        self.lab.pack()
        self.v = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.v)
        self.entry.pack()
        self.v.set(set_variable)

obj1 = Widgets("Enter website url: ", "https://www.google.com")
obj2 = Widgets("Enter width: ", "1024")
obj3 = Widgets("Enter height: ", "2048")
root.bind("<Return>", lambda x: main(obj1.v.get()), int(obj2.v.get()), int(obj3.v.get()))) 
lab4 = tk.Label(root, text="               ")
lab4.pack()

lab5 = tk.Label(root, text="Press the Enter key to create a screenshot")
lab5.pack()

root.mainloop()