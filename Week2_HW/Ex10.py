from Week2_HW.Ex9 import evaluate
from Week2_HW.Ex1 import create_board
from Week2_HW.Ex4 import random_place

def play_game():
    board = create_board()
    while evaluate(board) not in [1, 2, -1]:
        for player in [1, 2]:
            board = random_place(board, player)
            #print(board)


play_game()