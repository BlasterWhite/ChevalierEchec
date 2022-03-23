from tkinter import *
from tkinter.font import *
import tkinter


HAUTEUR = 800
LARGEUR = 800
CARRE_CASES = 6

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
        w.create_text((j * TAILLE_CASSE + TAILLE_CASSE/2), (i * TAILLE_CASSE + TAILLE_CASSE/2) , text = CASE, fill="#616161", font=FON_Police)
        CASE += 1
    if CARRE_CASES % 2 == 0:
        #print("Changement !", CARRE_CASES%2)
        if COULEUR == 1:
            COULEUR = 0
        else:
            COULEUR = 1
w.create_line(100,200,200,35, fill="black", width=3)
w.pack()

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()
