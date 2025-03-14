from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.configure(width=300, height=200)  # Adjusted for better appearance
root.configure(bg='black')

def calculate():
    try:
        # Get values from the entries
        weight = mass.get()
        height_value = height.get()
        
        # Calculate BMI
        BMI = BMI_val(weight, height_value)
        bmi_value.set(format(BMI, ".2f"))  # Set calculated BMI
        stat.set(getStatus(BMI))  # Set the status based on BMI
    except ZeroDivisionError:
        stat.set("Height cannot be zero.")
    except Exception as e:
        stat.set("Invalid input.")

def BMI_val(mass, height):
    return mass / height ** 2

def clear():
    stat.set('')
    bmi_value.set('0.0')
    mass_input.delete(0, 'end')
    height_input.delete(0, 'end')

def getStatus(BMI):
    if BMI > 40:
        return 'You are in Obese class 3'
    elif BMI > 30:
        return 'You are in Obese class 2'
    elif BMI > 30 and BMI <= 35:
        return 'You are in Obese class 1'
    elif BMI > 25 and BMI <= 30:
        return 'You are Overweight'
    elif BMI > 18.5 and BMI <= 25:
        return 'You are Normal'
    elif BMI > 17 and BMI <= 18.5:
        return 'You are Underweight'
    else:
        return 'Moderately Thin!'

height = DoubleVar()
h_label = Label(root, text="Height (m): ", bg='black', fg='red', font=('calibri', 15, 'bold'), pady=5, padx=8)
height_input = Entry(root, textvariable=height)
h_label.grid(row=0, column=0)
height_input.grid(row=0, column=1)

mass = DoubleVar()
w_label = Label(root, text="Mass (kg): ", bg='black', fg='red', font=('calibri', 15, 'bold'), pady=10, padx=2)
mass_input = Entry(root, textvariable=mass)
w_label.grid(row=1, column=0)
mass_input.grid(row=1, column=1)

bmi_value = StringVar()  # Changed to StringVar to hold formatted text
stat = StringVar()

bmi_label = Label(root, text='BMI: ', bg='black', fg='blue', font=('calibri', 15, 'bold'), pady=10, padx=2)
status_label = Label(root, text='Status: ', bg='black', fg='blue', font=('calibri', 15, 'bold'), pady=10, padx=2)
status_msg = Label(root, textvariable=stat, bg='black', fg='white', font=('calibri', 15, 'bold'), pady=10, padx=2)
BMI_total = Label(root, textvariable=bmi_value, bg='black', fg='white', font=('calibri', 15, 'bold'), pady=10, padx=2)

bmi_label.grid(row=2, column=0)
BMI_total.grid(row=2, column=1)
status_label.grid(row=3, column=0)
status_msg.grid(row=3, column=1)

calc_btn = Button(root, text="Calculate", bg='white', fg='black', font=('calibri', 15, 'bold'), command=calculate)
reset_btn = Button(root, text="Reset", bg='white', fg='black', font=('calibri', 15, 'bold'), command=clear)

calc_btn.grid(row=4, column=0)
reset_btn.grid(row=4, column=1)

root.mainloop()