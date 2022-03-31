from tkinter import *
from tkinter.font import *
import tkinter

def echiquier(HAUTEUR, LARGEUR, CARRE_CASES, board):
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tkinter.Canvas.create_circle = _create_circle

    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
    tkinter.Canvas.create_circle_arc = _create_circle_arc
    
    window = Tk()

    window.title("Echiquier")

    window.configure(width=LARGEUR, height=HAUTEUR)

    window.configure(bg='lightgray')

    TAILLE_CASSE = HAUTEUR/CARRE_CASES
    COULEUR = 0
    CASE = 1
    w = Canvas(window, width=HAUTEUR, height=LARGEUR)
    FON_Police = tkinter.font.Font (family = "arial" , size = "14")
    for i in range(CARRE_CASES):
        for j in range(CARRE_CASES):
            if COULEUR == 0:
                w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#E8EBEF", outline = 'gray')
                COULEUR = 1
            else:
                w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#7D8796", outline = 'gray')
                COULEUR = 0
            w.create_text((j * TAILLE_CASSE + TAILLE_CASSE/4), (i * TAILLE_CASSE + TAILLE_CASSE/4) , text = CASE, fill="#616161", font=FON_Police)
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
                    if i == 1:
                        x_prev = x
                        y_prev = y
                        w.create_circle(y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x_prev* TAILLE_CASSE + TAILLE_CASSE/2, TAILLE_CASSE/8, fill="red")
                        continue
                    w.create_line(y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x_prev* TAILLE_CASSE + TAILLE_CASSE/2, y* TAILLE_CASSE + TAILLE_CASSE/2 ,x* TAILLE_CASSE + TAILLE_CASSE/2 , fill="black", width=3)
                    #w.create_arc(x_prev* TAILLE_CASSE + TAILLE_CASSE/2 - 50, y_prev* TAILLE_CASSE + TAILLE_CASSE/2 - 50, x_prev* TAILLE_CASSE + TAILLE_CASSE/2 + 50, y_prev* TAILLE_CASSE + TAILLE_CASSE/2 + 50, 50, fill="blue", outline="#DDD",extent="135", width=4)
                    w.create_circle(y* TAILLE_CASSE + TAILLE_CASSE/2, x* TAILLE_CASSE + TAILLE_CASSE/2, TAILLE_CASSE/8, fill="red")
                    x_prev = x
                    y_prev = y

    w.pack()

    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))

    window.mainloop()

board = [
    [0,59,38,33,30,17,8,63],
    [37,34,31,60,9,62,29,16],
    [58,1,36,39,32,27,18,7],
    [35,48,41,26,61,10,15,28],
    [42,57,2,49,40,23,6,19],
    [47,50,45,54,25,20,11,14],
    [56,43,52,3,22,13,24,5],
    [51,46,55,44,53,4,21,12],
    
]

board2 = [
    [64, 9, 18, 31, 34, 39, 60, 1], 
    [17, 30, 63, 10, 61, 32, 35, 38], 
    [8, 19, 28, 33, 40, 37, 2, 59], 
    [29, 16, 11, 62, 27, 42, 49, 36], 
    [20, 7, 24, 41, 50, 3, 58, 43], 
    [15, 12, 21, 26, 55, 46, 51, 48], 
    [6, 25, 14, 23, 4, 53, 44, 57], 
    [13, 22, 5, 54, 45, 56, 47, 52]
]

board3 = [
    [14, 11, 26, 7, 16, 1], 
    [27, 6, 15, 12, 25, 34], 
    [10, 13, 8, 33, 2, 17], 
    [5, 28, 21, 24, 35, 32], 
    [20, 9, 30, 3, 18, 23], 
    [29, 4, 19, 22, 31, 36]
]

echiquier(800, 800, 6, board3)