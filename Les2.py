from tkinter import *
from tkinter.font import *
import tkinter

def echiquier(HAUTEUR, LARGEUR, CARRE_CASES, board, cycle):
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
                        x1 = x #Coordonné Origin x
                        y1 = y #Coordonné Origin y
                        w.create_circle(y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x_prev* TAILLE_CASSE + TAILLE_CASSE/2, TAILLE_CASSE/8, fill="blue")
                        continue
                    w.create_line(y_prev* TAILLE_CASSE + TAILLE_CASSE/2, x_prev* TAILLE_CASSE + TAILLE_CASSE/2, y* TAILLE_CASSE + TAILLE_CASSE/2 ,x* TAILLE_CASSE + TAILLE_CASSE/2 , fill="black", width=3)
                    w.create_circle(y* TAILLE_CASSE + TAILLE_CASSE/2, x* TAILLE_CASSE + TAILLE_CASSE/2, TAILLE_CASSE/8, fill="red")
                    x_prev = x
                    y_prev = y
    if cycle == True:
        w.create_line(y1* TAILLE_CASSE + TAILLE_CASSE/2, x1* TAILLE_CASSE + TAILLE_CASSE/2, y_prev* TAILLE_CASSE + TAILLE_CASSE/2 ,x_prev* TAILLE_CASSE + TAILLE_CASSE/2 , fill="black", width=3)
    w.pack()

    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))

    window.mainloop()

def creer_plateau(taille,voisin,plateau):
    ligne = [2,1,-1,-2,-2,-1,1,2]
    colonne = [1,2,2,1,-1,-2,-2,-1]  
    
    plateau = [[0 for j in range(taille) ] for k in range(taille)]
    n = 1
    
    for i in range (1,taille+1):
        for j in range (1,taille+1):
            plateau[i-1][j-1] = n
            n += 1
        
    for i in range (0,taille):
        for j in range (0,taille):
            voisin[plateau[i][j]] = []
            for k in range (0,8):
                if 0<=i+ligne[k]<taille and 0<=j+colonne[k]<taille:
                    voisin[plateau[i][j]].append(plateau[i+ligne[k]][j+colonne[k]])
    
    return voisin,plateau
    

def poid(ordre,voisin,sommet):
    compteur = 0
    for v in voisin[sommet]:
        if v not in ordre:
            compteur += 1
    return compteur


def affiche_plateau(plateau):
    for i in plateau:
        print(i)

def creer_matrice(ordre,taille,plateau):
    res = [[0 for j in range(taille) ] for k in range(taille)]

    for a in range (len(ordre)):
        for i in range (taille):
            for j in range (taille):
                if ordre[a] == plateau[i][j]:
                    res[i][j] = a+1
    
    return res 
        

def cavalier(taille, debut):
    # debut = random.randint(1,64)
    # debut = taille
    voisin,plateau = creer_plateau(taille, {}, [])
    affiche_plateau(plateau)
    resultat = cavalier_rec(taille,voisin,[],debut)
    print("---------",len(resultat[1]),"----------")
    if resultat[0]:
        affiche_plateau(creer_matrice(resultat[1],taille,plateau))
        return creer_matrice(resultat[1],taille,plateau)
    else:
        return None
    

def cavalier_rec(taille,voisin,ordre,suivi):
    ordre.append(suivi)
    print(suivi)
    if len(ordre) == taille*taille:
        return True,ordre
    

    voisin_possible =[]
    for i in voisin[suivi]:
        mini = (0,10)
        for j in voisin[suivi]:
            pd = poid(ordre,voisin,suivi)
            if pd<mini[1] and j not in ordre:
                if j not in voisin_possible:
                    mini = (j,pd)
        if mini[0] != 0:    
            voisin_possible.append(mini[0])
    voisin_possible.reverse()
    print("--",len(ordre))
    if voisin_possible == []:
        ordre.pop()
        return False,ordre
    
    
    for i in voisin_possible:
        res = cavalier_rec(taille,voisin,ordre,i)
        if res[0]:
            return res
    ordre.pop()
    return res


def tour_cavalier(taille, debut):
    # debut = random.randint(1,64)
    # debut = taille
    voisin,plateau = creer_plateau(taille, {}, [])
    affiche_plateau(plateau)
    resultat = tour_cavalier_rec(taille,voisin,[],debut,debut)
    print("---------",len(resultat[1]),"----------")
    if resultat[0]:
        affiche_plateau(creer_matrice(resultat[1],taille,plateau))
        return creer_matrice(resultat[1],taille,plateau)
    else:
        return None
    

def tour_cavalier_rec(taille,voisin,ordre,suivi,debut):
    ordre.append(suivi)
    print(suivi)
    if len(ordre) == taille*taille:
        if debut in voisin[suivi]:
            return True,ordre
        else:
            ordre.pop()
            return False,ordre
    

    voisin_possible =[]
    for i in voisin[suivi]:
        mini = (0,10)
        for j in voisin[suivi]:
            pd = poid(ordre,voisin,suivi)
            if pd<mini[1] and j not in ordre:
                if j not in voisin_possible:
                    mini = (j,pd)
        if mini[0] != 0:    
            voisin_possible.append(mini[0])
    voisin_possible.reverse()
    print("--",len(ordre))
    if voisin_possible == []:
        ordre.pop()
        return False,ordre
    
    
    for i in voisin_possible:
        res = tour_cavalier_rec(taille,voisin,ordre,i,debut)
        if res[0]:
            return res
    ordre.pop()
    return res



TAILLE_PLATEAU = 6
result = tour_cavalier(TAILLE_PLATEAU, 16)
if result != False:
    echiquier(800, 800, TAILLE_PLATEAU, result, True)