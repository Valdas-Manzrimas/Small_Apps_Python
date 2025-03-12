from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurnat management system")

Tops = Frame(root, bg="black", width=1600, height=500, relief="sunken")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief="sunken")
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief="sunken")
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('aria', 30, "bold"), text="Restaurant management system", fg="blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)

timeLabel = Label(Tops, font=('aria', 30, "bold"), text=localtime, fg="red", bg='black', anchor='w')
timeLabel.grid(row=1, column=0)


root.mainloop()