def CARRE(a):
    import numpy as np
    fichier=open("C:/Users/cl/Desktop/github/feu/"+a,"r")
    A=fichier.read()


    D=[]
    for i in range(0,len(A)):
        D.append(A[i])
    l=8 #nombre d'espace en fonction du nombre de ligne
    C=[]
    for i in range(0,len(D)):
        if D[i]==".":
            D[i]=1
            C.append(D[i])
        if D[i]=='x':
            C.append(D[i])

    for i in range(0,len(C)):
        if C[i]=='x':
            C[i]=2

    F=[]

    for i in range(0,l+1):
        F.append(C[27*i:27*(i+1)-1])


    X=[]
    for i in range(0,26):
        for j in range(0,len(F)):
            if F[j][i]==2:
                X.append([i,j])


    J=np.array(F)
    h=27 #nombre d'élément par ligne


    def erreur(B):
        if 2 in B:
            g="erreur"
        else:
            g="ok"
        return g

    k=0

    p=1
    for i in range(0,9):
        while erreur(J[i:p,0:p-i])=="ok":
            p=p+1
            J[i:p-1,0:p-i-1]
            


    p=1
    for j in range(0,27):
        while erreur(J[0:p,j:p+j])=="ok" and p <8:
            p=p+1
            J[0:p-1,j:p+j-1]

    l=0 #correspond à la longueur du plus grand
    a=0 ##correspond à la colonne du plus grand
    b=0 #correspond à la ligne du plus grand
    for i in range(0,9):
        p=1
        for j in range(0,26):
            if J[i][j]!=2:
                while erreur(J[i:p,j:p-i+j])=="ok" and p <100:
                    p=p+1     
                    if J[i:p-1,j:p-i+j-1].shape[0] == J[i:p-1,j:p-i+j-1].shape[1]:
                        J[i:p-1,j:p-i+j-1]
                        if len(J[i:p-1,j:p-i+j-1])>l:
                            l=len(J[i:p-1,j:p-i+j-1])
                            a=i
                            b=j

    for i in range(b,b+l+1):
        for j in range(a,a+l):
            J[j][i]=0
    print(J)

CARRE("carre.txt")