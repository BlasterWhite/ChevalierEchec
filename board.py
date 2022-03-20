import imp
from tkinter import *
from tkinter.font import *
import tkinter
from turtle import color, width
from typing import Counter

HAUTEUR = 800
LARGEUR = 800
CARRE_CASES = 8

window = Tk()
# set window title
window.title("Python GUI App")
# set window width and height
window.configure(width=LARGEUR, height=HAUTEUR)
# set window background color
window.configure(bg='lightgray')
"""
case0 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=0, row=0)
case1 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=1, row=1)
case2 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=2, row=2)
case3 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=3, row=3)
case4 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=4, row=4)
case5 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=5, row=5)
case6 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=6, row=6)
case7 = Label(window, width=int(LARGEUR/CARRE_CASES), height=int(HAUTEUR/CARRE_CASES), text="Test").grid(column=7, row=7)
"""
TAILLE_CASSE = HAUTEUR/CARRE_CASES
COULEUR = 0
CASE = 1
w = Canvas(window, width=HAUTEUR, height=LARGEUR)
FON_Police = tkinter.font.Font (family = "arial" , size = "14")
for i in range(CARRE_CASES):
    for j in range(CARRE_CASES):
        COULEUR += 1
        if COULEUR%2 != 0:
            w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#E8EBEF", outline = 'gray')
        else:
            w.create_rectangle((j * TAILLE_CASSE), (i * TAILLE_CASSE), (j * TAILLE_CASSE+TAILLE_CASSE), (i * TAILLE_CASSE+TAILLE_CASSE), fill="#7D8796", outline = 'gray')
        w.create_text((j * TAILLE_CASSE + 50), (i * TAILLE_CASSE + 50) , text = CASE, fill="#616161", font=FON_Police)
        CASE += 1
    COULEUR += 1

w.pack()

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))


window.mainloop()