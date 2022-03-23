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

board = np.zeros((CARRE_CASES, CARRE_CASES))

#Creation du Canvas
w = Canvas(window, width=HAUTEUR, height=LARGEUR)

# Appel de la fonction Cherche
if cherche(board, CARRE_CASES, 1, 3, 4):
    FON_Police = tkinter.font.Font (family = "arial" , size = "14")
    COULEUR = 0
    CASE = 1
    for i in range(CARRE_CASES):
        for y in range(CARRE_CASES):
            print(board[i][y], " ")
        print("\n")

    #Création Echiquier
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
                    print("Trouve ", i)
                    trouve = True
                    if i == 0:
                        x_prev = x
                        y_prev = y
                    elif i == 1: # 1 b'est pas généré
                        continue
                    else:
                        print("Dessin une ligne de ", i, " | ", x_prev, ", ", y_prev, ", ", x, ", ", y,)
                        w.create_line(x_prev* TAILLE_CASSE + TAILLE_CASSE/2, y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x* TAILLE_CASSE + TAILLE_CASSE/2 ,y* TAILLE_CASSE + TAILLE_CASSE/2 , fill="black", width=3)
                        x_prev = x
                        y_prev = y

    w.pack()
else:
    print('Pas de solution')
    FON_Police = tkinter.font.Font (family = "arial" , size = "48")
    w.create_text((LARGEUR/2), (HAUTEUR/2) , text = 'Pas de solution', fill="#616161", font=FON_Police)






winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()
