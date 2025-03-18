import tkinter as tk

class tictactoe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)

        self.btns = []
        self.turn = True
        self.count = 0

        self.Board()

    def Board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(self, width=10, height=3, font=("Calibri", 35, "bold"), bg="white", command=lambda x=i, y=j: self.Turn_Taken(x, y)))

                row[j].grid(row=i, column=j)
            self.btns.append(row) 
        tk.Button(self, text="Restart", width=10, height=1, font=("Calibri", 15, "bold"), bg="black", fg="white", activebackground="grey", activeforeground="green", command=self.NewGame).grid(row=3, column=1)

    def Turn_Taken(self, x, y):
        self.count += 1
        if self.turn:
            char = "X"
            self.btns[x][y].config(text="X", bg="light green", state="disabled")
        else:
            char = "O"
            self.btns[x][y].config(text="O", bg="pink", state="disabled")
        self.Check_Results(char)
        self.turn = not self.turn

    def NewGame(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.btns = []
        self.turn = True
        self.count = 0

        self.Board()

    def Check_Results(self, char):
           # horizontal
        if(((self.btns[0][0]['text'] == char) and (self.btns[0][1]['text'] == char) and (self.btns[0][2]['text'] == char)) or ((self.btns[1][0]['text'] == char) and (self.btns[1][1]['text'] == char) and (self.btns[1][2]['text'] == char)) or ((self.btns[2][0]['text'] == char) and (self.btns[2][1]['text'] == char) and (self.btns[2][2]['text'] == char)) or 
           # vertical
           ((self.btns[0][0]['text'] == char) and (self.btns[1][0]['text'] == char) and (self.btns[2][0]['text'] == char)) or ((self.btns[0][1]['text'] == char) and (self.btns[1][1]['text'] == char) and (self.btns[2][1]['text'] == char)) or ((self.btns[0][2]['text'] == char) and (self.btns[1][2]['text'] == char) and (self.btns[2][2]['text'] == char)) or 
           # diagnal
           ((self.btns[0][0]['text'] == char) and (self.btns[1][1]['text'] == char) and (self.btns[2][2]['text'] == char)) or ((self.btns[0][2]['text'] == char) and (self.btns[1][1]['text'] == char) and (self.btns[2][0]['text'] == char))
        ):
            self.Result(char)
        elif self.count == 9:
            self.Result("Draw") 
            


tictactoe().mainloop()