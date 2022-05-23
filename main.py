#%%
3+4
# %%
import random
from board import Board
#%%
s = (1,7)
board = Board()

board.squares[1][7] = -1
board.squares[6][7] = 1
board.squares[2][6]= -6
board.squares[2][6]= 6


#board.check_if_in_check()
#for i in board.get_valid_piece_moves(s):
#    board.squares[i[0]][i[1]] = 9

test = board.get_valid_pawn_moves(s)
for s in board.squares:
    print(s)
for i in test:
    board.squares[i[0]][i[1]] = 9
print()
for s in board.squares:
    print(s)

# %%
