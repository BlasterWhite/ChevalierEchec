moveLigne = [2,1,-1,-2,-2,-1,1,2]
movecolone = [1,2,2,1,-1,-2,-2,-1]

def bonPlacement(board, ligne, colone, n):
   return ligne >=0 and colone >=0 and ligne < n and colone < n and board[ligne][colone] == 0

def cherche(board, n, move_no, currligne, currcolone):
    if move_no == n*n:
        return True
    for i in range(8):
        nextligne = currligne + moveLigne[i]
        nextcolone = currcolone + movecolone[i]
        if bonPlacement(board, nextligne, nextcolone, n):
            board[nextligne][nextcolone] = move_no + 1
            c_est_correct = cherche(board, n, move_no+1, nextligne, nextcolone)
            if c_est_correct:
                return True
            board[nextligne][nextcolone] = 0
    return False

n = 6
board = [[0 for i in range(n)] for i in range(n)]
if cherche(board, n, 1, 0, 0):
    print(board)
else:
    print('Pas de solution')