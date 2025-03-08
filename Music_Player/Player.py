from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import os

# Initialize the mixer
mixer.init()

# Create the main window
window = Tk()
window.geometry("600x350")  # Increased height to accommodate the status bar
window.title("Music Player")

# Global variables
current_directory = os.path.expanduser("~/Music")
file_name = ""
paused = False

# Menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

def open_dir():
    global current_directory
    current_directory = filedialog.askdirectory()
    populate_music_directory(current_directory)

sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Open", command=open_dir)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=window.quit)

def play_action():
    """Play the selected MP3 file."""
    global paused
    try:
        if paused:
            mixer.music.unpause()
            statusbar['text'] = f"Playing: {file_name}"
        else:
            mixer.music.load(file_name)
            mixer.music.play()
            statusbar['text'] = f"Playing: {file_name}"
            paused = False
    except Exception as e:
        print("Error on music play:", e)
        messagebox.showerror("Error", "File not found or unable to play")

def stop_action():
    mixer.music.stop()
    statusbar['text'] = 'Stopped'

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def pause_action():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = 'Paused'

def rewind_action():
    play_action()

# Create frames for layout
top_frame = Frame(window)
top_frame.pack(side=TOP, fill=X)

main_frame = Frame(top_frame)
main_frame.pack(side=RIGHT, padx=10, pady=10)

menu_frame = Frame(top_frame)
menu_frame.pack(side=LEFT)

# Listbox and scrollbar for music files
scrollbar = Scrollbar(menu_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(menu_frame, width=40, height=20)
listbox.pack(side=LEFT, fill=BOTH, expand=True)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def populate_music_directory(directory):
    """Populate the Listbox with MP3 files and folders in the given directory."""
    listbox.delete(0, END)  # Clear the current listbox
    try:
        if directory != os.path.expanduser("~/Music"):
            listbox.insert(END, ".. (Back to Parent Directory)")

        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path) and item.lower().endswith('.mp3'):
                listbox.insert(END, item)
            elif os.path.isdir(item_path):
                listbox.insert(END, item)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_item_double_click(event):
    """Handle double-click events on Listbox items."""
    selected_item_index = listbox.curselection()
    if selected_item_index:
        selected_item = listbox.get(selected_item_index)
        global current_directory

        if selected_item == ".. (Back to Parent Directory)":
            current_directory = os.path.dirname(current_directory)
        else:
            selected_item_path = os.path.join(current_directory, selected_item)
            if os.path.isdir(selected_item_path):
                current_directory = selected_item_path
            else:
                global file_name
                file_name = selected_item_path
                play_action()

        populate_music_directory(current_directory)

populate_music_directory(current_directory)

listbox.bind('<Double-1>', on_item_double_click)

# Main frame content
button_frame = Frame(main_frame)
button_frame.pack(padx=40)

# Control buttons
photo = PhotoImage(file='play.png')
play_btn = Button(button_frame, image=photo, command=play_action)  
play_btn.pack(side=LEFT, padx=(10, 5))

stop_img = PhotoImage(file='stop.png')
stop_btn = Button(button_frame, image=stop_img, command=stop_action)
stop_btn.pack(side=LEFT, padx=(5, 5))

pause_img = PhotoImage(file='pause.png')
pause_btn = Button(button_frame, image=pause_img, command=pause_action)
pause_btn.pack(side=LEFT, padx=(5, 10))

scale = Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.pack()

button_frame2 = Frame(main_frame)
button_frame2.pack(padx=40)

rewind_img = PhotoImage(file='rewind.png')
rewind_btn = Button(button_frame2, image=rewind_img, command=rewind_action)
rewind_btn.pack(side=LEFT, padx=(10, 20))

# Status bar at the bottom
statusbar = Label(window, text="Enjoy :)", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# Start the main loop
window.mainloop()