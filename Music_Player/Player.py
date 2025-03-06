from tkinter import *
from pygame import mixer

window = Tk()

mixer.init()

window.geometry("300x300")
window.title("Music Player")

txt_label = Label(window, text="Music Player", font=("Arial", 20))
txt_label.pack()

def play_action():
    mixer.music.load('play.mp3')
    mixer.music.play()

def stop_action():
    mixer.music.stop()

button_frame = Frame(window)
button_frame.pack(padx=40)

photo = PhotoImage(file='play.png')
play_btn = Button(button_frame, image=photo, command=play_action)  
play_btn.pack(side=LEFT, padx=(10, 5))

stop_img = PhotoImage(file='stop.png')
stop_btn = Button(button_frame, image=stop_img, command=stop_action)
stop_btn.pack(side=RIGHT, padx=(5, 10))

 



window.mainloop()