from Week2_HW.Ex1 import create_board

def place(board, player, position):
    if board[position[0]][position[1]] == 0:
        board[position[0]][position[1]] = player
    return board


#board = create_board()
#board = place(board, 1, (0, 0))

#print(board)