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

        



tictactoe().mainloop()