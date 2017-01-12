import random
from Week2_HW.Ex3 import possibilities


def random_place(board, player):
    p = possibilities(board)
    choice = random.choice(p)
    board[choice[0], choice[1]] = player
    return board

