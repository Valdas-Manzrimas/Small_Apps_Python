import tkinter as tk

class tictactoe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x400")
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

    



tictactoe().mainloop()