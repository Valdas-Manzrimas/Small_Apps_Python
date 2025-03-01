from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def application(root):
    root.geometry('{}x{}'.format(700, 600))
    root.resizible(width=False, height=False)
    root.title('PDF2 Audio')

    root.configure(background='light grey')

    global rate, male, female

    #Frame1
    frame1 = Frame(root, width=500, height=200, bg="indigo")

    #Frame2
    frame2 = Frame(root, width=500, height=450, bg="light grey")

    frame1.pack(side=TOP, fill=BOTH)
    frame2.pack(side=TOP, fill=Y)

    #frame1 widgets
    name1 = Label(frame1, text="PDF to Audio", bg="light grey", fg="black", font=("Arial", 20))
    name1.pack()

    name2 = Label(frame1, text="Hear a PDF file", bg="green", fg="black", font=("calibri", 25, "bold"))
    name2.pack()

    #frame2 widgets
    btn = Button(frame2, text="Select PDF", bg="black", fg="white", activeforeground='red', padx=70, pady=10, font=("Arial", 12, "bold"), command=lambda: extract_text())
    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Rate of speech", bg="aqua", fg="black", font=("Arial 12", 15))
    rate_text.grid(row=1, column=0, pady=15, padx=10, sticky=W)

    rate = Entry(frame2, text="150", fg='black', bg='white', font=("Arial", 12))
    rate.grid(row=1, column=1, pady=15, padx=30, sticky=W)

    voice_text = Label(frame2, text="Select voice:", bg="aqua", fg="black", font=("Arial 12", 15))
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)

    male = IntVar()
    maleOpt = Checkbutton(frame2, text="Male", bg="pink", fg="black", font=("Arial 12", 15), variable=male, onvalue=1, offvalue=0)
    maleOpt.grid(row=2, column=1, pady=0, padx=30, sticky=W)
    female = IntVar()
    femaleOpt = Checkbutton(frame2, text="Female", bg="pink", fg="black", font=("Arial 12", 15), variable=female, onvalue=1, offvalue=0)
    femaleOpt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submitBtn = Button(frame2, text="Play PDF file", bg="black", fg="white", activeforeground='red', padx=60, pady=10, font=("Arial", 12, "bold"), command=lambda: speak_text())
    submitBtn.grid(row=4, column=0, pady=65)