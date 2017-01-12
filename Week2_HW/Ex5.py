from Week2_HW.Ex1 import create_board
from Week2_HW.Ex4 import random_place

board = create_board()
for i in range(3):
    for player in [1, 2]:
        board = random_place(board, player)

print(board)