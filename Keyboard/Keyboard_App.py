import tkinter as tk 

Keyboard = tk.Tk()
Keyboard.title("Keyboard App")

keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "="
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "DEL"
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", '"',
    "z", "x", "c", "v", "b", "n", "m", ",", ".", "!", "TAB",
    "SPACE"]

curBtn = [-1, -1]
buttonL = [[]]
entry = tk.Text(Keyboard, width=97, height=8)
entry.grid(row=0, columnspan=15)

varRow = 1
varColumn = 0

for button in keys:
    if button != "SPACE":
        btn = tk.Button(Keyboard, text=button, width=5, bg='black', fg='white', highlightthickness=4, activebackground='gray', activeforeground='red', highlightcolor='red', relief='raised', padx=12, pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: selelct(x, i, j))

        btn.bind('<<Return>>', lambda event, x=button, i=varRow-1, j=varColumn: selelct(x, i, j))
        buttonL[varRow-1].append(btn) 
        btn.grid(row=varRow, column=varColumn)

    if button == "SPACE":
        btn = tk.Button(Keyboard, text=button, width=60, bg='black', fg='white', highlightthickness=4, activebackground='gray65', activeforeground='red', highlightcolor='red', relief='raised', padx=4, pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: selelct(x, i, j))

        btn.bind('<<Return>>', lambda event, x=button, i=varRow-1, j=varColumn: selelct(x, i, j))
        buttonL[varRow-1].append(btn) 
        btn.grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])



Keyboard.mainloop()
                        
