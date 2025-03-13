from tkinter import *
import tkinter as tk
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurnat management system")

def btnclick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def clear_display():
    global operator
    operator = ''
    text_input.set('')

def equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''

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

class fBtn:
    def __init__(self, parent, text, command, row, column):
        self.fBtn = tk.Button(parent, text=text, command=command, bg='black', fg='white', bd=10, relief='raised', width=10, height=2, padx=16, pady=8, font=('Ariel', 16, 'bold'))
        self.fBtn.grid(row=row, column=column)

fBtn(f1, 'TOTAL', ref, 7, 1)
fBtn(f1, 'RESET', reset, 7, 2)
fBtn(f1, 'EXIT', qexit, 7, 3)

def price():
    roo = Tk()
    roo.geometry('600x220')
    roo.title('Price List')
    x = Frame(roo, bg='white', width=600, height=220, relief='sunken')
    x.pack(side=TOP)

    lblInfo = Label(x, font=('aria', 15, 'bold'), text='ITEM', fg='red', bd=5)
    lblInfo.grid(row=0, column=0)
    
    lblInfo = Label(x, font=('aria', 15, 'bold'), text='_________', fg='black', anchor='w')
    lblInfo.grid(row=0, column=2)

    lblInfo = Label(x, font=('aria', 15, 'bold'), text='PRICE', fg='black', bd=5, anchor='w')
    lblInfo.grid(row=0, column=5)

    class priceLabel:
        def __init__(self, text, row, column):
            self.label = tk.Label(x, font=('aria', 15, 'bold'), text=text, fg='black', anchor='w')
            self.label.grid(row=row, column=column)

    priceLabel('Fries Meal', 1, 0)
    priceLabel('25', 1, 5)
    priceLabel('Lunch Meal', 2, 0)
    priceLabel('40', 2, 5)
    priceLabel('Burger Meal', 3, 0)
    priceLabel('35', 3, 5)
    priceLabel('Pizza Meal', 4, 0)
    priceLabel('50', 4, 5)
    priceLabel('Cheesburger', 5, 0)
    priceLabel('30', 5, 5)
    priceLabel('Drinks', 6, 0)
    priceLabel('35', 6, 5)

    roo.mainloop()

fBtn(f1, 'PRICE', price, 7, 0)

        

root.mainloop()