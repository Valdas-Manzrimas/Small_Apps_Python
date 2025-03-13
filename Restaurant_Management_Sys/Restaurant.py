from tkinter import *
import tkinter as tk
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurnat management system")

def btnclick(value):
    print(f'Button clicked: {value}')  # Replace with your actual logic

def clear_display():
    print('Display cleared')  # Replace with your actual logic

def equals():
    print('Calculate result')  # Replace with your actual logic

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

# Calculator GUI
class CalculatorButton:
    def __init__(self, parent, text, row, column, command):
        self.button = tk.Button(parent,
                                 padx=16,
                                 pady=16,
                                 fg='white',
                                 font=('Ariel', 20, 'bold'),
                                 text=text,
                                 bg='black',
                                 command=command)
        self.button.grid(row=row, column=column)

text_input = StringVar()
operator = ""

txt_display = Entry(f2, font=('Ariel', 20, 'bold'), textvariable=text_input, bd=5, bg='lightgreen', insertwidth=7, justify='right')
txt_display.grid(columnspan=4)

CalculatorButton(f2, '7', 2, 0, lambda: btnclick(7))
CalculatorButton(f2, '8', 2, 1, lambda: btnclick(8))
CalculatorButton(f2, '9', 2, 2, lambda: btnclick(9))
CalculatorButton(f2, '+', 2, 3, lambda: btnclick('+'))

CalculatorButton(f2, '4', 3, 0, lambda: btnclick(4))
CalculatorButton(f2, '5', 3, 1, lambda: btnclick(5))
CalculatorButton(f2, '6', 3, 2, lambda: btnclick(6))
CalculatorButton(f2, '-', 3, 3, lambda: btnclick('-'))

CalculatorButton(f2, '1', 4, 0, lambda: btnclick(1))
CalculatorButton(f2, '2', 4, 1, lambda: btnclick(2))
CalculatorButton(f2, '3', 4, 2, lambda: btnclick(3))
CalculatorButton(f2, '*', 4, 3, lambda: btnclick('*'))

CalculatorButton(f2, '0', 5, 0, lambda: btnclick(0))
CalculatorButton(f2, 'C', 5, 1, clear_display)
CalculatorButton(f2, '.', 5, 2, lambda: btnclick('.'))
CalculatorButton(f2, '/', 5, 3, lambda: btnclick('/'))

btnEqual = Button(f2, padx=16, pady=16, fg='white', font=('Ariel', 20, 'bold'), text='=', bg='black', command=equals)
btnEqual.grid(columnspan=4)

# Input frame GUI

rand = StringVar()
fries = StringVar()
lunch = StringVar()
burger = StringVar()
pizza = StringVar()
subTotal = StringVar()
total = StringVar()
service_charge = StringVar()
drinks = StringVar()
tax = StringVar()
cost = StringVar()
cheese_burger = StringVar()

class InputRow:
    def __init__(self, parent, label_text, row, column, text_variable):
        # Create a label
        self.label = tk.Label(parent, font=("arial", 16, 'bold'), text=label_text, fg='black', bd=10, anchor='w')
        self.label.grid(row=row, column=column)

        # Create an entry
        self.entry = tk.Entry(parent, font=('arial', 17, 'bold'), textvariable=text_variable, bd=6, insertwidth=4, bg='red', justify='right')
        self.entry.grid(row=row, column=column+1)

InputRow(f1, 'Order_No: ', 0, 0, rand)
InputRow(f1, 'Fries Meal: ', 1, 0, fries)
InputRow(f1, 'Lunch Meal: ', 2, 0, lunch)
InputRow(f1, 'Burger Meal: ', 3, 0, burger)
InputRow(f1, 'Pizza Meal: ', 4, 0, pizza)
InputRow(f1, 'Cheese Burger: ', 5, 0, cheese_burger)
InputRow(f1, 'Drinks: ', 0, 2, drinks)
InputRow(f1, 'Cost: ', 1, 2, cost)
InputRow(f1, 'Service Charge: ', 2, 2, service_charge)
InputRow(f1, 'Tax: ', 3, 2, tax)
InputRow(f1, 'Subtotal: ', 4, 2, subTotal)
InputRow(f1, 'Total: ', 5, 2, total)



root.mainloop()