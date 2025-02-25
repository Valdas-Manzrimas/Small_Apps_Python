import tkinter
import socket
from tkinter import *
from threading import Thread

def receive():
    while True: # as long as client is receiving messages
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg:
                break
            msg_list.insert(tkinter.END, msg)
        except Exception as e:
            print(f"An error occurred while receiving a message: {e}")
            break
    sock.close()
    window.quit()

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

def send_with_enter(event):
    send()

window = Tk()
window.title("Chat Room Application") 
window.configure(bg="#2ecc71")

window.protocol("WM_DELETE_WINDOW", on_closing)

message_frame = Frame(window, height=300, width=500, bg="#e74c3c")
message_frame.pack(padx=5, pady=5)

my_msg=StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=60, yscrollcommand=scroll_bar.set, font=("Arial", 12), highlightthickness=0)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

input_frame = Frame(window)
input_frame.pack()

label = Label(input_frame, text="Message:", bg="#2ecc71", fg="#3498db", font=("Arial", 12, "italic"))
label.pack(side=tkinter.LEFT)

entry_field = Entry(input_frame, textvar=my_msg, font=("Arial", 12, "italic"), width=50)
entry_field.bind("<Return>", send_with_enter)
entry_field.pack(side=tkinter.LEFT)

button_frame = Frame(window)
button_frame.pack()

send_button = Button(button_frame, text="Send", font=("Arial", 12, "bold"), width=10, command=send)
send_button.pack(side=tkinter.LEFT)

quit_button = Button(button_frame, text="Quit", font=("Arial", 12, "bold"), width=10, command=on_closing)
quit_button.pack(side=tkinter.LEFT)
# connect to server
Host='localhost'
Port=8080   

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((Host,Port))

receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()
