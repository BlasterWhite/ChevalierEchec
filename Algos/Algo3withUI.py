from tkinter import *
from tkinter.font import *
import tkinter
import numpy as np

HAUTEUR = 800
LARGEUR = 800
CARRE_CASES = 6

TAILLE_CASSE = HAUTEUR/CARRE_CASES

window = Tk()
window.title("Echiquier")
window.configure(width=LARGEUR, height=HAUTEUR)
window.configure(bg='lightgray')

#Creation du Canvas
w = Canvas(window, width=HAUTEUR, height=LARGEUR)

 
def isSafe(x, y, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if(x >= 0 and y >= 0 and x < CARRE_CASES and y < CARRE_CASES and board[x][y] == -1):
        return True
    return False
 
 
def printSolution(n, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
 
 
def solveKT(n):
    '''
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    '''
 
    # Initialization of Board matrix
    board = [[-1 for i in range(n)]for i in range(n)]
 
    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    # Since the Knight is initially at the first block
    board[0][0] = 0
 
    # Step counter for knight's position
    pos = 1

    COULEUR = 0
    CASE = 1
 
    # Checking if solution exists or not
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
        FON_Police = tkinter.font.Font (family = "arial" , size = "48")
        w.create_text((LARGEUR/2), (HAUTEUR/2) , text = 'Pas de solution', fill="#616161", font=FON_Police)
    else:
        printSolution(n, board)
        #Création Echiquier
        FON_Police = tkinter.font.Font (family = "arial" , size = "14")
        for i in range(CARRE_CASES):
            for j in range(CARRE_CASES):
                if COULEUR == 0:
                    w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#E8EBEF", outline = 'gray')
                    COULEUR = 1
                else:
                    w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#7D8796", outline = 'gray')
                    COULEUR = 0
                w.create_text((j * TAILLE_CASSE + TAILLE_CASSE/2), (i * TAILLE_CASSE + TAILLE_CASSE/2) , text = CASE, fill="#616161", font=FON_Police)
                CASE += 1
            if CARRE_CASES % 2 == 0:
                #print("Changement !", CARRE_CASES%2)
                if COULEUR == 1:
                    COULEUR = 0
                else:
                    COULEUR = 1

        #Création de la ligne de Graph
        for i in range(CARRE_CASES*CARRE_CASES+1):
            for x in range(CARRE_CASES):
                for y in range(CARRE_CASES):
                    if board[x][y] == i:
                        #print("Trouve ", i)
                        if i == 0:
                            x_prev = x
                            y_prev = y
                    elif i == 1: # 1 b'est pas généré
                        continue
                    else:
                        #print("Dessin une ligne de ", i, " | ", x_prev, ", ", y_prev, ", ", x, ", ", y,)
                        w.create_line(x_prev* TAILLE_CASSE + TAILLE_CASSE/2, y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x* TAILLE_CASSE + TAILLE_CASSE/2 ,y* TAILLE_CASSE + TAILLE_CASSE/2 , fill="black", width=3)
                        x_prev = x
                        y_prev = y

                w.pack()

        winWidth = window.winfo_reqwidth()
        winwHeight = window.winfo_reqheight()
        posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
        window.geometry("+{}+{}".format(posRight, posDown))

        window.mainloop()

 
 
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''
 
    if(pos == n**2):
        return True
 
    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
 
            # Backtracking
            board[new_x][new_y] = -1
    return False
 
 
# Driver Code
if __name__ == "__main__":
     
    # Function Call
    solveKT(CARRE_CASES)
 
# This code is contributed by AAKASH PAL