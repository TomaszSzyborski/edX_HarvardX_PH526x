import numpy as np
#from Week2_HW.Ex1 import board

def col_win(board, player):
    for i in range(3):
        if np.all(board[:,i] == player):
            return True
    return False

#col_win(board, 1)