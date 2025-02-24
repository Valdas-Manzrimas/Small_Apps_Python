import tkinter
import socket
from tkinter import *
from threading import Thread

def receive():
    while True: # as long as client is receiving messages
        try:
            msg = sock.recv(1024).decode('utf-8')
            msg_list.insert(tkinter.END, msg)
        except:
            print("An error occured while receiving a message!")
            break

def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg, "utf-8"))
    if msg == "#quit":
        sock.close()
        window.close()

def on_closing():
    my_msg.set("#quit")
    send()
    sock.close()
    window.destroy()

window = Tk()
window.title("Chat Room Application") 
window.configure(bg="green")

message_frame = Frame(window, height=300, width=500, bg="red")
message_frame.pack()

my_msg=StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, yscrollcommand=scroll_bar.set, bg="white")

scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter Message", bg="lightgreen", fg="blue", font=("Arial", 12, "italic"))
label.pack()

entry_field = Entry(window, textvar=my_msg, font=("Arial", 12, "italic"), width=50)
entry_field.pack()

send_button = Button(window, text="Send", font=("Arial", 12, "bold"), width=10, command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font=("Arial", 12, "bold"), width=10, command=on_closing)
quit_button.pack()

# connect to server
Host='localhost'
Port=8080   

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((Host,Port))

receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()
