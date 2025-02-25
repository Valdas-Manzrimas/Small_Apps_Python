from tkinter import *
import smtplib
import re

def login():
    if validate_login():
        global username
        global password
        username = str(entry1.get())
        password = str(entry2.get())
        global server
        # create insecure connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
    
        server.starttls() # make connection secure
        server.login(username, password)

        f2.grid()
        btn2.grid()
        label4['text'] = 'Login successful'
        root.after(10, root.grid)
        f1.grid_remove()
        root.after(10, root.grid)
        f3.grid()
        label9.grid_remove()
        root.after(10, root.grid)

def hide_login_label():
    f2.grid_remove()
    f3.grid_remove()
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

def logout():
    try:
        server.quit()
        f3.grid_remove()
        f2.pack()
        label4.grid()
        label4['text'] = 'Logged Out successful'
        btn2.grid_remove()
        f1.grid()
        entry2.delete(0, END)
        root.after(10, root.grid)
    except Exception as e:
        label4['text'] = 'Error occured while logging out'

def validate_login():
    email_text = str(entry1.get())
    pass_text = str(entry2.get())
    if (email_text == '' or pass_text == ''):
        f2.grid()
        label4.grid()
        label4['text'] = 'Please fill all required fields'
        btn2.grid_remove()
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if not EMAIL_REGEX.match(email_text):
            f2.grid()
            label4.grid()
            label4['text'] = 'Enter a valid email address'
            btn2.grid_remove()
            root.after(10, root.grid)
            return False
        else:
            return True

def validate_message():
    email_text = str(entry3.get())
    subject_text = str(entry4.get())
    msg_text = str(entry5.get())
    if (email_text == '' or subject_text == '' or msg_text == ''):
        label9.grid()
        label9['text'] = 'Please fill all required fields'
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[ˆ@\s]+@[ˆ@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            label9.grid()
            label9['text'] = 'Enter a valid email address'
            root.after(10, root.grid)
            return False
        elif(len(subject_text < 3) or len(msg_text < 3)):
            label9.grid()
            label9['text'] = 'Enter at least 3 characters in subject and message'
            root.after(10, root.grid)
            return False
        else:
            return True

root = Tk()
root.title("Email Application")

# Frame 1
f1 = Frame(root)
f1.grid(row=0, column=0)

label1 = Label(f1, width=25, text='Enter your credentials', font=('calibri', 18, 'bold'))
label1.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, text='Email')
label2.grid(row=1, column=0, sticky=E, padx=5, pady=10)

label3 = Label(f1, text='Password')
label3.grid(row=2, column=0, sticky=E, padx=5, pady=10)

entry1 = Entry(f1)
entry1.grid(row=1, column=1, pady=5)

entry2 = Entry(f1, show='*')
entry2.grid(row=2, column=1)

btn1 = Button(f1, text="Login", width=10, bg='black', fg='white', command=lambda: login())
btn1.grid(row=3, column=0, columnspan=3, pady=10)

# Frame 2
f2 = Frame(root)
f2.grid(row=1, column=0)

label4 = Label(f2, width=20, text='Login successful', bg='light green', fg='white', font=('calibri', 12, 'bold'))
label4.grid(row=0, column=0, columnspan=2,  pady=5)

btn2 = Button(f2, text="X", bg="red", fg="white", command=lambda: logout())
btn2.grid(row=0, column=2, sticky=E, pady=10, padx=(5, 0))

# Frame 3
f3 = Frame(master=root)
f3.grid(row=2, column=0)

label5 = Label(f3, width=20, text='Compose email', font=('calibri', 18, 'bold'))
label5.grid(row=0, column=0, columnspan=3, pady=10)

label6 = Label(f3, text='To')
label6.grid(row=1, column=0, sticky=E, pady=5)

label7 = Label(f3, text='Subject')
label7.grid(row=2, column=0, sticky=E, pady=5)

label8 = Label(f3, text='Message')
label8.grid(row=3, column=0, sticky=E)

entry3 = Entry(f3)
entry3.grid(row=1, column=1, pady=5)

entry4 = Entry(f3)
entry4.grid(row=2, column=1, pady=5)

entry5 = Entry(f3)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3 = Button(f3, text="Send", width=10, bg='black', fg='white', command=lambda: send_mail())
btn3.grid(row=6, column=0, columnspan=3, pady=10)

label9 = Label(f3, width=20, bg='light green', fg='white', font=('calibri', 18, 'bold'))
label9.grid(row=7, column=0, columnspan=3, pady=5)

hide_login_label()

root.mainloop()