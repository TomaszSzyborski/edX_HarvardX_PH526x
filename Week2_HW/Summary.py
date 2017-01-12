import numpy as np
import random

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position[0]][position[1]] == 0:
        board[position[0]][position[1]] = player
    return board

def possibilities(board):
    return np.where(board == 0)

def random_place(board, player):
    p = possibilities(board)
    p = [tup for tup in zip(*p)]
    choice = random.choice(p)
    board[choice[0], choice[1]] = player
    return board

def col_win(board, player):
    for i in range(3):
        if np.all(board[:,i] == player):
            return True
    return False

def row_win(board, player):
    for i in range(3):
        if np.all(board[i,:] == player):
            return True
    return False

def diag_win(board, player):
    return (np.all(np.diag(board) == player)) or (np.all(np.diag(np.fliplr(board)) == player))

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if np.any(np.array([row_win(board, player), col_win(board, player), diag_win(board,player)]) == True):
            winner=player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            board = random_place(board, player)
            #print("board after random placement")
            #print(board)
            winner = evaluate(board)
            #print("winner:")
            #print(winner)
            if winner in [-1, 1, 2]:
                return winner


print(play_game())

import time

game_len = []
time.time()
for i in range(1000):
    before = time.time()
    play_game()
    after = time.time()
    game_len.append(after - before)

print(game_len)
