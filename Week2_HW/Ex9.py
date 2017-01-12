import numpy as np
from Week2_HW.Ex6 import row_win
from Week2_HW.Ex7 import col_win
from Week2_HW.Ex8 import diag_win
#from Week2_HW.Ex1 import board

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if np.all([row_win(board, player), col_win(board, player), diag_win(board,player)] == True):
            winner=player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

#print(evaluate(board))
