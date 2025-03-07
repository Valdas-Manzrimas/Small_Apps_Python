from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import os

window = Tk()

mixer.init()

window.geometry("300x300")
window.title("Music Player")

def browse_file():
    global fileName
    fileName = ""
    fileName = filedialog.askopenfilename(initialdir=f"{os.path.expanduser('~')}/Music")


menu_bar = Menu(window)
window.config(menu=menu_bar)

sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=sub_menu)

sub_menu.add_command(label="Open", command=browse_file)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=window.quit)

txt_label = Label(window, text="Music Player", pady=10, font=("Arial", 20))
txt_label.pack()

def play_action():
    try:
        paused
       
    except:
        try:
            mixer.music.load(fileName)
            mixer.music.play()
        except:
            print("Error on music play")
            messagebox.showerror("Error", "Dile not found")
    else: 
        mixer.music.unpause()
        
def stop_action():
    mixer.music.stop()

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def pause_action():
    global paused
    paused = True
    mixer.music.pause()

button_frame = Frame(window)
button_frame.pack(padx=40)

photo = PhotoImage(file='play.png')
play_btn = Button(button_frame, image=photo, command=play_action)  
play_btn.pack(side=LEFT, padx=(10, 5))

stop_img = PhotoImage(file='stop.png')
stop_btn = Button(button_frame, image=stop_img, command=stop_action)
stop_btn.pack(side=RIGHT, padx=(5, 5))

pause_img = PhotoImage(file='pause.png')
pause_btn = Button(button_frame, image=pause_img, command=pause_action)
pause_btn.pack(side=RIGHT, padx=(5, 10))

scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.pack()

 



window.mainloop()