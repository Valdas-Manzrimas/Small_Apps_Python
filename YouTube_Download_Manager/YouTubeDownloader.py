from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import re
import threading

class Application:
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg="#CCFFF7")

        top_label = Label(self.root, text='YouTube Downloader', font=('Type Xerophim', 46, 'bold'), fg='orange', bg="#CCFFF7")
        top_label.grid(pady=(0, 10))

        link_label = Label(self.root, text='YouTube Url:', font=('Garamond', 30, 'bold'), fg='green', bg="#CCFFF7")
        link_label.grid(pady=(0, 20))

        self.YouTubeEntryVar = StringVar()

        self.youtubeEntry = Entry(self.root, width=70, textvariable=self.YouTubeEntryVar, font=('Agenta', 25, 'italic'), fg='red', bg="#CCFFF7")
        self.youtubeEntry.grid(pady=(0, 15), ipady=2)

if __name__=="__main__":
    window = Tk()
    window.title("YouTube Downloader")
    window.state("zoomed")

    app = Application(window)

    mainloop()