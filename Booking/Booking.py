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