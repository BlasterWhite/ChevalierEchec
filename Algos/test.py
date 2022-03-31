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
        
            
        

def cavalier(taille):
   # debut = random.randint(1,64)
    debut = taille
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
        
        
print(cavalier(6))