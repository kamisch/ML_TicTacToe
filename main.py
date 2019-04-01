from game import Game
from player import Player
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

bot1_sym = 'O'
bot2_sym = 'X'

def optimize_bot(game, bot1, bot2):
    """
    Punish or Reward the bot with respect to the agent that wins the game
    """
    if game.winner == bot1_sym:
        bot1.on_reward(1)
        # reward
        bot2.on_reward(-1)
        # punishment
    elif game.winner == bot2_sym:
        bot1.on_reward(-1)
        bot2.on_reward(1) 
    
def train(epochs, bot1, bot2):
    bot1_wins = 0
    bot2_wins = 0
    win_trace = pd.DataFrame(data=np.zeros((epochs, 2)), columns=['bot1', 'bot2'])
    for i in range(epochs):
        print('-' * 100)
        print('epoch: {}'.format(i + 1))
        game = Board()
        while not game.stale:
            # Exit if the board is full
            
            winner = game.player_move(bot2_sym, *bot2.select_move(game.board))
            if winner:
                optimize_bot(game, bot1, bot2)
                bot2_wins += 1
                win_trace.set_value(i, 'bot2', 1)
                break
                win_trace[i] = 2
            elif winner == 'draw':
                break
    return win_trace, bot1_wins, bot2_wins
bot = Agent()
bot2 = Agent()
epochs = 5000
win_trace, bot1_wins, bot2_wins = train(epochs, bot, bot2)