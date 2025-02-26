from pytubefix import YouTube
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

        self.downloadBtn = Button(self.root, text='Download', width=10,font=('Calibri', 15), command=self.checkYoutubeLink)
        self.downloadBtn.grid(pady=(30, 5))

    def checkYoutubeLink(self):
        self.matchYoutubeLink = re.match("^https://www.youtube.com/.", self.YouTubeEntryVar.get())
        if (not self.matchYoutubeLink):
            self.youtubeEntryError.config(text="Invalid YouTube Link", fg="red")
        elif (not self.openDirectory):
            self.youtubeFileSaveLabel.config(text="Please Choose directory", fg="red")
        elif (self.matchYoutubeLink and self.openDirectory):
            self.downloadWindow()

    def downloadWindow(self):
        self.newWindow = Toplevel(self.root)
        self.root.withdraw()
        self.newWindow.state("zoomed")
        self.newWindow.grid_rowconfigure(0, weight=0)
        self.newWindow.grid_columnconfigure(0, weight=1)

        self.app = SecondApp(self.newWindow, self.YouTubeEntryVar.get(), self.FolderName, self.ChoicesVar.get())

    def openDirectory(self):
        self.FolderName = filedialog.askdirectory()

        if len(self.FolderName) > 0:
            self.youtubeFileSaveLabel.config(text=self.FolderName,fg="green")
            return True
        else:
            self.youtubeFileSaveLabel.config(text="Please choose directory",fg="red")

class SecondApp:
    def __init__(self, downloadWindow, youtubeLink, folderName, choices):

        self.downloadWindow = downloadWindow
        self.youtubeLink = youtubeLink
        self.folderName = folderName
        self.choices = choices

        self.yt = YouTube(self.youtubeLink)

        if (choices=="1"):
            self.video_type = self.yt.streams.filter(only_audio=True).first()
            self.maxFileSize = self.video_type.filesize

        if (choices=="2"):
            self.video_type = self.yt.streams.first()
            self.maxFileSize = self.video_type.filesize

        self.loadingLabel = Label(self.downloadWindow, text="Downloading...", font=("Small fonts", 40), bg="#CCFFF7")
        self.loadingLabel.grid(pady=(100, 0 ))
        
        self.loadingPercent = Label(self.downloadWindow, text="0", font=("Agency FB", 40), fg='green')
        self.loadingPercent.grid(pady=(50, 0))

        self.progressBar = ttk.Progressbar(self.downloadWindow, length=500, orient='horizontal', mode='indeterminate')
        self.progressBar.grid(pady=(50, 0))
        self.progressBar.start()

        threading.Thread(target=self.yt.register_on_progress_callback(self.showProgress)).start()  
        threading.Thread(target=self.downloadFile).start()

    def downloadFile(self): 
        
        if(self.choices=="1"):
            self.yt.streams.filter(only_audio=True).first().download(self.folderName)
        if(self.choices=="2"):
            self.yt.streams.first().download(self.folderName)

    def showProgress(self, streams=None, chunk=None, file_handle=None, bytes_remaining=None):

        self.percentCount = float("%0.2f"% (100-(100*(bytes_remaining/self.maxFileSize))))
        if (self.percentCount<100):
            self.loadingPercent.config(text=f"{self.percentCount}%")
        else:
            self.progressBar.stop()
            self.loadingLabel.grid_forget()
            self.progressBar.grid_forget()

            self.downloadFinished = Label(self.downloadWindow, text="Download Finished", font=("yardman", 40), bg="#CCFFF7")
            self.downloadFinished.grid(pady=(150, 0))

            self.downloadFileName = Label(self.downloadWindow, text=self.yt.title , font=("Small fonts", 30))
            self.downloadFileName.grid(pady=(50, 0))

            MB = float("%0.2f"% (self.maxFileSize/1000000))

            self.downloadedFileSize = Label(self.downloadWindow, text=str(f"{MB} MB"), font=("Agency FB", 30))
            self.downloadedFileSize.grid(pady=(50, 0))

if __name__=="__main__":
    window = Tk()
    window.title("YouTube Downloader")
    window.state("zoomed")

    app = Application(window)

    mainloop()