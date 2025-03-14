from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.configure(width=100, height=100)
root.configure(bg='black')

height = DoubleVar()
h_label = Label(root, text="Height: ", bg='black', fg='red', font=('calibri', 15, 'bold'), pady=5, padx=8)

height_input = Entry(root, textvariable=height)
h_label.grid(row=2, column=0)
height_input.grid(row=2, column=1, columnspan=2, padx=5)

mass = DoubleVar()
w_label = Label(root, text="Mass: ", bg='black', fg='red', font=('calibri', 15, 'bold'), pady=10, padx=2)
mass_input = Entry(root, textvariable=mass)
w_label.grid(row=4, column=0)
mass_input.grid(row=4, column=1, columnspan=2, padx=5)

bmi_value = DoubleVar()
stat = StringVar()

bmi = Label(root, text='BMI: ', bg='black', fg='blue', font=('calibri', 15, 'bold'), pady=10, padx=2, justify=LEFT)
stat = Label(root, text='Status', bg='black', fg='blue', font=('calibri', 15, 'bold'), pady=10, padx=2)
status_msg = Label(root, textvariable=stat, bg='black', fg='white', font=('calibri', 15, 'bold'), pady=10, padx=2)
BMI_total = Label(root, textvariable=bmi_value, bg='black', fg='white', font=('calibri', 15, 'bold'), pady=10, padx=2)

bmi.grid(row=6)
stat.grid(row=7)
BMI_total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

calc_btn = Button(root, text="Calculate", bg='white', fg='black', font=('calibri', 15, 'bold'), command=calculate)
reset_btn = Button(root, text="Reset", bg='white', fg='black', font=('calibri', 15, 'bold'), command=clear)
calc_btn.grid(row=8)
calc_btn.grid(row=8, column=3)


root.mainloop()