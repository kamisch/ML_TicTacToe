#tic tac toe main
import numpy as np
class Game:
    def __init__(self,player1,player2):
        self.board = np.matrix('e e e; e e e; e e e')
        self.move = 0
        self.player1 = player1
        self.player2 = player2
        self.winner = None

