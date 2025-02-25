from tkinter import *
import smtplib
import re

def login():
    if validate_login():
        global username
        global password # global only for learning purposes
        username = str(entry1.get())
        password = str(entry2.get())
        global server
        # create insecure connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
    
        server.starttls() # make connection secure
        server.login(username, password)

        f2.pack()
        btn2.grid()
        label4['text'] = 'Login successful'
        root.after(10, root.grid)
        f1.pack_forget()
        root.after(10, root.grid)
        f3.pack()
        label9.grid_remove()
        root.after(10, root.grid)

def hide_login_label():
    f2.pack_forget()
    f3.pack_forget()
    root.after(10, root.grid)

def send_mail():
    if validate_message():
        label9.grid_remove()
        root.after(10, root.grid)
        receiver = str(entry3.get())
        subject = str(entry4.get())
        msgbody = str(entry5.get())
        msg = 'From: ' + username + '\nTo: ' + receiver + '\nSubject: ' + subject + '\n\n' + msgbody
        try:
            server.sendmail(username, receiver, msg)
            label9.grid()
            label9['text'] = 'Email sent'
            root.after(10, label9.grid)
        except Exception as e:
            label9.grid()
            label9['bg'] = 'red'
            label9['text'] = 'Error occured while sending email'
            root.after(10, label9.grid)



root = Tk()
root.title("Email Application")

# Frame 1
f1 = Frame(root, width=1000 , height=800)
f1.pack(side=TOP)

label1 = Label(width=25, text='Enter your credentials', font=('calibri', 18, 'bold'))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, text='Email').grid(row=1, sticky=E, padx=5, pady=10)
label3 = Label(f1, text='Password').grid(row=2, sticky=E, padx=5, pady=10)

entry1 = Entry(f1)
entry2 = Entry(f1, show='*')

entry1.grid(row=1, column=1, pady=5)
entry2.grid(row=2, column=1)

btn1 = Button(f1, text="Login", width=10, bg='black', fg='white', command=lambda: login())
btn1.grid(row=3, columnspan=3, pady=10)

# Frame 2
f2 = Frame(root)
f2.pack(side=TOP, expand=NO, fill=NONE)

label4 = Label(f2, width=20, text='Login successful', bg='light green', fg='white', font=('calibri', 12, 'bold'))
label4.grid(row=0, column=0, columnspan=2,  pady=5)

btn2 = Button(f2, text="X", bg="red", fg="white", command=lambda: logout())
btn2.grid(row=0, column=4, sticky=E, pady=10, padx=(5, 0))

# Frame 3
f3 = Frame(master=root)
f3.pack(side=TOP, expand=NO, fill=NONE)

label5 = Label(f3, width=20, text='Compose email', font=('calibri', 18, 'bold'))
label5.grid(row=0, columnspan=3, pady=10)

label6 = Label(f3, text='To').grid(row=1, sticky=E, pady=5)
label7 = Label(f3, text='Subject').grid(row=2, sticky=E, pady=5)
label8 = Label(f3, text='Message').grid(row=3, sticky=E)

entry3 = Entry(f3)
entry4 = Entry(f3)
entry5 = Entry(f3)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3 = Button(f3, text="Send", width=10, bg='black', fg='white', command=lambda: send_mail())
btn3.grid(row=6, columnspan=3, pady=10)

label9 = Label(f3, width=20, bg='light green', fg='white', font=('calibri', 18, 'bold'))
label9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()