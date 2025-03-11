import tkinter as tk 

Keyboard = tk.Tk()
Keyboard.title("Keyboard App")

keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "=",
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "DEL",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", '"',
    "z", "x", "c", "v", "b", "n", "m", ",", ".", "!", "TAB",
    "SPACE"]

curBtn = [-1, -1]
buttonL = [[]]
entry = tk.Text(Keyboard, width=97, height=8)
entry.grid(row=0, columnspan=15)

varRow = 1
varColumn = 0

def leftKey(event):
    if curBtn == [-1, -1]:
        curBtn[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBtn[0] == 4:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [0, 10]
        buttonL[0][10].configure(highlightbackground='red')
    else:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [curBtn[0], (curBtn[1]-1)%11]
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    buttonL[curBtn[0]][curBtn[1]].focus_set()
    

def rightKey(event):
    if curBtn == [-1, -1]:
        curBtn[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBtn[0] == 4:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground='red')
    else:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [curBtn[0], (curBtn[1]+1)%11]
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    buttonL[curBtn[0]][curBtn[1]].focus_set()

def upKey(event):
    if curBtn == [-1, -1]:
        curBtn[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBtn[0] == 0:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]-1)%5, 0] 
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    elif curBtn[0] == 4:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]-1)%5, 5]
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    else:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]-1)%5, curBtn[1]]
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    buttonL[curBtn[0]][curBtn[1]].focus_set()

def downKey(event):
    if curBtn == [-1, -1]:
        curBtn[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBtn[0] == 3:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]+1)%5, 0] 
        buttonL[curBtn[0]][curBtn[1]%11].configure(highlightbackground='red')
    elif curBtn[0] == 4:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]+1)%5, 5]
        buttonL[curBtn[0]][curBtn[1]%11].configure(highlightbackground='red')
    else:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        curBtn[:] = [(curBtn[0]+1)%5, curBtn[1]]
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
    buttonL[curBtn[0]][curBtn[1]].focus_set()


def select(value, x, y):
    if curBtn != [-1, -1]:
        buttonL[curBtn[0]][curBtn[1]].configure(highlightbackground='red')
        buttonL[curBtn[0]][curBtn[1]].configure(highlightcolor='red')
    curBtn[:] = [x,y]
    buttonL[x][y].configure(highlightbackground='red')
    buttonL[x][y].configure(highlightcolor='red')

    if value == "DEL":
        input_val = entry.get("1.0", "end-2c")
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")
    elif value == "SPACE":
        entry.insert("insert", " ")
    elif value == 'TAB':
        entry.insert("insert", "    ")
    else:
        entry.insert("end", value)
    
   

for button in keys:
    if button != "SPACE":
        btn = tk.Button(Keyboard, text=button, width=5, bg='black', fg='white', highlightthickness=4, activebackground='gray', activeforeground='red', highlightcolor='red', relief='raised', padx=12, pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))

        btn.bind('<<Return>>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(btn) 
        btn.grid(row=varRow, column=varColumn)

    if button == "SPACE":
        btn = tk.Button(Keyboard, text=button, width=60, bg='black', fg='white', highlightthickness=4, activebackground='gray65', activeforeground='red', highlightcolor='red', relief='raised', padx=4, pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))

        btn.bind('<<Return>>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(btn) 
        btn.grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])


Keyboard.bind('<Left>', leftKey)
Keyboard.bind('<Right>', rightKey)
Keyboard.bind('<Up>', upKey)
Keyboard.bind('<Down>', downKey)
Keyboard.bind('<Return>', lambda _: select(keys[curBtn[0] * 11 + curBtn[1]], curBtn[0], curBtn[1]))

Keyboard.mainloop()
                        

