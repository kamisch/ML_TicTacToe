from game import Game
from player import Player

end = False
player1 = Player()
player2 = Player()
new_game = Game(player1,player2)
while(not end):
    print(new_game.board)
