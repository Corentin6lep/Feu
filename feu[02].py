
def MAT(a):
    def matrice(a):
        fichier=open("C:/Users/cl/Desktop/github/feu/"+ a , "r")
        A=fichier.read()
        l=(len(A)+1)/5 #représente le nombre de lignes de quatre chiffres
        l=int(l)
        a=4*l+(l-1) #le nombres de chiffres avec le vide


        C=[]
        for i in range(0,len(A)):
            C.append(A[i])
        D=[]

        for i in range(0,len(C)):
            if  C[i]==" ":
                C[i]=0
            if C[i]!="\n":
                C[i]=int(C[i])

        for i in range(0,l):
            D.append(C[5*i:5*(i+1)-1])
        return D,l



    def Cherch(a):
        fichier=open("C:/Users/cl/Desktop/github/feu/"+ a , "r")
        A=fichier.read()
        l=(len(A)+1)/5 #représente le nombre de lignes de quatre chiffres
        l=int(l)
        a=4*l+(l-1) #le nombres de chiffres avec le vide


        C=[]

        for i in range(0,len(A)):
            C.append(A[i])
        D=[]

        for i in range(0,len(C)):
            if  C[i]==" ":
                C[i]=0
            if C[i]!="\n":
                C[i]=int(C[i])

        for i in range(0,l+1):
            D.append(C[3*i:3*(i+1)-1])
        return D


    E=matrice("plateau.txt")[0]
    l=matrice("plateau.txt")[1]
    print(E)

    F=Cherch("a trouver.txt")
    print(F)

    for j in range(0,l-1):
        for i in range(1,4):
            if F[0][1] == E[j][4-i] and F[1][1] == E[j+1][4-i] and F[0][0] == E[j][4-i-1]:
                print('trouvé en coordonnées:(',4-i-1 ,";",j ,')')

MAT("a trouver.txt")