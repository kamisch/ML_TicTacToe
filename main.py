from game import Game
from player import Player

player1 = Player("O")
player2 = Player("X")
new_game = Game(player1,player2)
new_game.start()
new_game.play()
