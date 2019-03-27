#tic tac toe main
import numpy as np
class Game:
    def __init__(self,player1,player2):
        self.board = np.matrix('0 0 0; 0 0 0; 0 0 0')
        self.move = 0
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.starter = None
        self.challenger = None
    def start(self):
        whoStarts = np.random.randint(2, size=1)
        if whoStarts[0] == 0:
            self.starter = self.player1
            self.challenger = self.player2
        else:
            self.starter = self.player2
            self.challenger = self.player1
    