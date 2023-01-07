def resolv(a):
    fichier=open("C:/Users/cl\Desktop/github/feu/"+a,"r")
    A=fichier.read()

    B=[]
    G=['.'," ",'\n']

    N=[1,2,3,4,5,6,7,8,9]

    C=[]
    for i in range(0,len(A)):
        C.append(A[i])

    for i in range(0,len(C)):
        if C[i] not in G:
            C[i]=int(C[i])

    for i in range(0,9):
        B.append(C[10*i:10*(i+1)-1])


    C=[] #par colonne
    for j in range(0,len(B)):
        for i in range(0,len(B)):
            C.append(B[i][j])

    D=[]
    for i in range(0,9):
        D.append(C[9*i:9*(i+1)])

    V=[]
    for i in range(0,len(B)):
        for j in range(0,len(B)):
                if B[i][j]==".":
                    V.append([i,j]) 


    for l in range(0,len(V)):
        B[int(V[l][0])][int(V[l][1])]=9


    def erreur(i):
        m=B[int(V[i][0])][int(V[i][1])]
        B[int(V[i][0])][int(V[i][1])]=0
        D[int(V[i][1])][int(V[i][0])]=0
        if m in B[int(V[i][0])] or m in D[V[i][1]]:
            g="True"
        
        else:
            g="False"
        B[int(V[i][0])][int(V[i][1])]=m
        D[int(V[i][1])][int(V[i][0])]=m
        return g
    

    MP=[]
    for i in range(0,19):
        MP.append(i)
    
    MP=200*MP

    def glok(m):
        for i in range(MP[m],MP[len(V)+m]):
            while erreur(i) == "True" and sum(B[int(V[i][0])])!=45:
                B[int(V[i][0])][int(V[i][1])]=B[int(V[i][0])][int(V[i][1])]-1
        return B
    
    B=glok(0)
    MP=[]
    for i in range(0,19):
        MP.append(i)
    
    MP=200*MP

    def glok(m):
        for i in range(MP[m],MP[len(V)+m]):
            while erreur(i) == "True" and sum(B[int(V[i][0])])!=45:
                B[int(V[i][0])][int(V[i][1])]=B[int(V[i][0])][int(V[i][1])]-1
        return B
    
    B=glok(0)
    

    c=0
    d=0
    for i in range(0,len(V)):
        if B[int(V[i][0])][int(V[i][1])] ==-1:
            c=c+1
        if B[int(V[i][0])][int(V[i][1])] == 9:
            d=d+1

    i=1
    while c!=0 and d>10:
        B=glok(i)
        for l in range(0,len(V)):
            B[int(V[l][0])][int(V[l][1])]=9   
        c=0
        d=0
        for i in range(0,len(V)):
            if B[int(V[i][0])][int(V[i][1])] ==-1:
                c=c+1
            if B[int(V[i][0])][int(V[i][1])] == 9:
                d=d+1
        i=i+1 

    for m in range(0,len(B)):
        print(B[m])

resolv("sudoku.txt")