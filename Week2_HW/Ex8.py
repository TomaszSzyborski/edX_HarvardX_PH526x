import numpy as np
#from Week2_HW.Ex1 import board

def diag_win(board, player):
    return (np.all(np.diag(board) == player)) or (np.all(np.diag(np.fliplr(board)) == player))

#diag_win(board, 1)