import numpy as np

move_x = [2, 2, 1,-1,-2,-2, 1,-1,]
move_y = [1,-1, 2, 2, 1,-1,-2,-2,]

def validateMove(board, row, col, n):
    if row < n and row >= 0 and col < n and col >= 0 and board[row,col] == 0:
        return True



def solve(board, row, col, n, counter):

    for i in range(n):
        if counter >= 65:
            return True
    
        new_x = row + move_x[i]
        new_y = col + move_y[i]

        if validateMove(board, new_x, new_y, n):
            board[new_x, new_y] = counter
            if solve(board, new_x, new_y, n, counter+1):
                return True
            board[new_x, new_y] = 0
    #print("Test pour piece N°", counter, " en ", new_x, ",", new_y)
    return False

n = 6

board = np.zeros((n,n))

board[3, 4] = 1
print(solve(board, 3, 2, n, 2))
print(board)

"""
import numpy as np

move_x = [2, 2, 1,-1,-2,-2, 1,-1,]
move_y = [1,-1, 2, 2, 1,-1,-2,-2,]

def validateMove(board, row, col):
    if row < 8 and row >= 0 and col < 8 and col >= 0 and board[row,col] == 0:
        return True



def solve(board, row, col, n, counter, best):

    for i in range(8):
        if counter >= 65:
            return True
    
        new_x = row + move_x[i]
        new_y = col + move_y[i]
        
        if validateMove(board, new_x, new_y):
            board[new_x, new_y] = counter
            if solve(board, new_x, new_y, n, counter+1, best):
                return True
            board[new_x, new_y] = 0
    #print("Test pour piece N°", counter, " en ", new_x, ",", new_y)
    return False

board = np.zeros((8,8))

board[3, 2] = 1
solve(board, 3, 2, 8, 2, 999)
print(board.sum())
"""