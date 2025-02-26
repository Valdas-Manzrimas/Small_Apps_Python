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

        self.youtubeEntryError = Label(self.root, text="", font=("Concert One", 20), bg="#CCFFF7", fg="red")
        self.youtubeEntryError.grid(pady=(0, 8))

        self.youtubeFileSaveLabel = Label(self.root, text='Choose directory', font=('Concert One', 30, 'bold'), fg='black', bg="#CCFFF7")
        self.youtubeFileSaveLabel.grid()

        self.youtubeFileDeirectoryBtn = Button(self.root, text='Directory', font=('Bell MT', 15), command=self.openDirectory)
        self.youtubeFileDeirectoryBtn.grid(pady=(10, 3))

        self.youtubeFileSaveLabel = Label(self.root, text='', font=('Franklin Gothic', 25,), bg="#CCFFF7")
        self.youtubeFileSaveLabel.grid()

        self.youtubeChooseLabel = Label(self.root, text="Choose download type", font=('Variety', 20))
        self.youtubeChooseLabel.grid()

        self.downloadChoices = [("Audio MP3", 1), ("Video MP4", 2)]

        self.ChoicesVar = StringVar()
        self.ChoicesVar.set(1)

        for text,mode in self.downloadChoices:
            self.youtubeChoices = Radiobutton(self.root, text=text, variable=self.ChoicesVar, value=mode)
            self.youtubeChoices.grid()



    def openDirectory(self):
        self.FolderName = filedialog.askdirectory()

        if len(self.FolderName) > 0:
            self.youtubeFileSaveLabel.config(text=self.FolderName,fg="green")
            return True
        else:
            self.youtubeFileSaveLabel.config(text="Please choose directory",fg="red")
            



if __name__=="__main__":
    window = Tk()
    window.title("YouTube Downloader")
    window.state("zoomed")

    app = Application(window)

    mainloop()