from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Music Player")

txt_label = Label(window, text="Play", font=("Arial", 20))
txt_label.pack()

photo = PhotoImage(file='play.png')

pic_label = Label(window, image=photo)
pic_label.pack()

window.mainloop()