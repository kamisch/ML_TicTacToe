#agent
class Player:
    def __init__(self,symbol):
        self.symbol = symbol
        self.nextMove = None
        self.moveInd = 0
        self.board = None
    def move(self,board):
        self.board = board
        
        
