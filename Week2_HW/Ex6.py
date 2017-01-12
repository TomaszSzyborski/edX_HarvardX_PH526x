#from Week2_HW.Ex1 import board
import numpy as np
def row_win(board, player):
    #board = np.array(board)
    #print(board[2,:])
    #print(board[:,2])
    for i in range(3):
        if np.all(board[i,:] == player):
            return True
    return False

#print(row_win(board, 1))