#tic tac toe main
import numpy as np
class Game:
    def __init__(self,n=3,player_sym="x"):
        self.board = None
        self.set_board(n)
        self.move = 0
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.starter = None
        self.challenger = None
    def set_board(self,n):
        self.board = np.zeros((n,n)).astype(int)
        self.winner = None
    def start(self):
        whoStarts = np.random.randint(2, size=1)
        if whoStarts[0] == 0:
            self.starter = self.player1
            self.challenger = self.player2
        else:
            self.starter = self.player2
            self.challenger = self.player1
    def play(self):
        end = False
        while(not end):
            print(self.board)