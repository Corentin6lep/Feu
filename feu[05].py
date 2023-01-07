def LAB(a):
    import numpy as np
    fichier=open("C:/Users/cl/Desktop/github/feu/"+a,"r")
    A=fichier.read()

    D=[]
    for i in range(0,len(A)):
        D.append(A[i])

    F=[]
    for i in range(0,10): #10 est le nombre de colonne
        F.append(D[12*i:12*(i+1)-2]) #11 élément par ligne

    F=np.array(F)

    X=[] #les arrivés
    for i in range(0,10):
        for j in range(0,10):
            if F[j][i]=="2":
                X.append((j,i))


    D=[] #le départ
    for i in range(0,10):
        for j in range(0,10):
            if F[j][i]=="1":
                D.append([i,j])



    CF=[]
    def find_paths(matrix, start, end, path=[]):
        # ajout de la position courante au chemin
        path = path + [start]
        
        # si la position courante est la position d'arrivée, on imprime le chemin et on arrête la recherche
        if start == end:
            CF.append(path)
        else:
            # sinon, on parcours récursivement les cases adjacentes
            x, y = start
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                # vérification que la nouvelle position est bien dans la matrice et qu'elle n'a pas déjà été visitée
                if 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0]) and (x+dx, y+dy) not in path and F[x+dx][y+dy] !='*':
                    find_paths(matrix, (x+dx, y+dy), end, path)

    for x in X:
        find_paths(F, (D[0][1], D[0][0]), x)



    l=CF[0]
    for i in CF:
        if len(i)<=len(l):
            l=i
    print(l)



    for x in l:
        F[x]=0
    F[D[0][1]][D[0][0]]=1

    for k in X:
        F[k]=2


    print(F,"EN ", len(l)-2, "COUPS !")

LAB("laby.txt")