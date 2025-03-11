import tkinter as tk
import tkinter.ttk

screens = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]

movies = {"Horror": ["Hereditary", "A Quiet Place", "The Conjuring 2", "The Grudge", "Anabelle Comes Home"], 
          "Action": ["Avengers End Game", "JOhn Wick Chapter 3", "Aquamen", "Black Panther", "Mission Impossible "],
          "Drama": ["Joker", "Spotlight", "Little Women", "The Irish Man", "Parasite", "Once Upon a Time in Hollywood"],
          "Comedy": ["Step Brothers", "BookSmart", "Horrible Bosses", "Superbad", "The Hangover", "The Hangover Part 2", "The Hangover Part 3"],
          "Sci-Fi": ["Inception", "Interstellar", "The Martian", "The Dark Knight Rises", "The Dark Knight"],
          "Romance": ["The Notebook", "The Proposal", "The Fault In Our Stars", "Titanic", "The Tourist"]
          }

times = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

seatList = []
seatSelected = []

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinema Booking")
        self.createWidgets()
    
    def updateMovies(self, event=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]

    def createWidgets(self):
        headingLabel = tk.Label(self, text="Cinema Booking", font=("Aries 12 bold"))
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky="w")

        day = tk.Frame(self)
        tk.Label(day, text="_____", ).pack()
        tk.Label(day, text="Today", font=("Aries 10 underline")).pack()
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)

        tk.Label(self, text="Genre: ").grid(row=2, column=1, padx=(10, 0))
        self.genreCombo = tkinter.ttk.Combobox(self, width=15, values=list(movies.keys()), state="readonly")

        self.genreCombo.set("Select Genre")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=2, column=2)

        tk.Label(self, text="Movie: ").grid(row=2, column=3, padx=(10, 0))
        self.movieCombo = tkinter.ttk.Combobox(self, width=15, state="readonly")
        self.movieCombo.bind('<<ComboboxSelected>>', self.createTimeButtons)
        self.movieCombo.set("Select Movie")
        self.movieCombo.grid(row=2, column=4, padx=(10, 0))
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky="w")


app = Application()

app.mainloop()