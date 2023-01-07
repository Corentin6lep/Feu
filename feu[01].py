def somme(g):
    def mat(a):
        b=[]
        j=0
        c=0
        for i in range(0,len(a)):
            b.append(a[i])
            if a[i]== '(':
                j=j+i
                while a[i] !=')':
                    c=c+1
                    i=i+1
        Ag=b[0:j]
        Ain=b[j+1: j+c]
        Ad=b[j+c+1:]
        return Ag,Ain,Ad


    def concat(A):
        j=0
        c=0
        d=0

        B=[]
        for i in range(0, len(A)):
            if A[i] == " ":
                j=j+i
                d=j-c
                c=j
                j=0
                if d<2:
                    B.append(A[0])
                else:
                    d>=2
                    g=''.join(A[i-d:i])
                    B.append(g)
        return B
    


    def Gauche(A):
        P=[' *',' /',' %',' +',' -']
        G=[' *',' /',' %']
        M=[' +',' -']
        l=[]
        if A[len(A)-1] in P:
            del A[len(A)-1]
        A.append('z')
        if A[0] not in M:
            j=0
            m=0
            for i in range(0,len(A)):
                if (A[i] == " *" or A[i] == " /" or A[i] == " %" or A[i] == ' +' or A[i] == " -" ) and A[i+1]!= 'z':
                    A[i-1]=int(A[i-1])
                    A[i+1]=int(A[i+1])

        if A[1] not in G:
            l.append(A[0])
        
    

    

        for i in range(1, len(A)-2):
            if A[i] == ' *' and A[i-2] != ' -':
                l.append(A[i-1]*A[i+1])
            if A[i] == ' *' and A[i-2] == ' -':
                l.append(-A[i-1]*A[i+1])
            if A[i] == ' /' and A[i-2] != ' -':
                l.append(A[i-1]/A[i+1])
            if A[i] == ' /' and A[i-2] == ' -':
                l.append(-A[i-1]/A[i+1])
            if A[i] == ' %' and A[i-2] != ' -':
                l.append(A[i-1]%A[i+1])
            if A[i] == ' %' and A[i-2] == ' -':
                l.append(-A[i-1]%A[i+1])
            if (A[i]==' -' and A[i+2] not in G) or (A[i]==' -' and A[i+2]== 'z'):
                l.append(-A[i+1])
            if (A[i]==' +' and A[i+2] not in G) or (A[i]==' +' and A[i+2]== 'z'):
                l.append(A[i+1])
                
        return l


    def Droite(A):
        P=[' *',' /',' %',' +',' -']
        G=[' *',' /',' %']
        M=[' +',' -']
        l=[]
        A.append('z')
        
        if A[0] not in M:
            for i in range(0,len(A)):
                if (A[i] == " *" or A[i] == " /" or A[i] == " %" or A[i] == ' +' or A[i] == " -" ) :
                    A[i+1]=int(A[i+1])
                    
        
        

        for i in range(1, len(A)-2):
            if A[i] == ' *' and A[i-2] != ' -':
                l.append(A[i-1]*A[i+1])
            if A[i] == ' *' and A[i-2] == ' -':
                l.append(-A[i-1]*A[i+1])
            if A[i] == ' /' and A[i-2] != ' -':
                l.append(A[i-1]/A[i+1])
            if A[i] == ' /' and A[i-2] == ' -':
                l.append(-A[i-1]/A[i+1])
            if A[i] == ' %' and A[i-2] != ' -':
                l.append(A[i-1]%A[i+1])
            if A[i] == ' %' and A[i-2] == ' -':
                l.append(-A[i-1]%A[i+1])
            if A[i]==' -' and A[i+2] not in G:
                l.append(-A[i+1])
            if A[i]==' +' and A[i+2] not in G:
                l.append(A[i+1])
                
        return l

    V=[]
    for i in mat(g):
        V.append(i)

    V0=concat(V[0])
    V1=concat(V[1])
    V2=concat(V[2])

    V00=Gauche(V0)
    V11=Gauche(V1)
    V22=Droite(V2)

    somme1=0
    somme2=0
    if V[0][len(V[0])-2]== "*" and V[2][1] == "+":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "*" and V[2][1] == "-":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "*" and V[2][1] == "/":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== "*" and V[2][1] == "%":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) %sum(V22)
    if V[0][len(V[0])-2]== "*" and V[2][1] == "*":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) *sum(V22)


    if V[0][len(V[0])-2]== "/" and V[2][1] == "+":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "/" and V[2][1] == "-":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "/" and V[2][1] == "/":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== "/" and V[2][1] == "%":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) %sum(V22)
    if V[0][len(V[0])-2]== "/" and V[2][1] == "*":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) *sum(V22)


    if V[0][len(V[0])-2]== "%" and V[2][1] == "+":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "%" and V[2][1] == "-":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "%" and V[2][1] == "/":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== "%" and V[2][1] == "%":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) %sum(V22)
    if V[0][len(V[0])-2]== "%" and V[2][1] == "*":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) *sum(V22)




    if V[0][len(V[0])-2]== "+" and V[2][1] == "+":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "+" and V[2][1] == "-":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "+" and V[2][1] == "/":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== "+" and V[2][1] == "%":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) %sum(V22)
    if V[0][len(V[0])-2]== "+" and V[2][1] == "*":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) *sum(V22)

    if V[0][len(V[0])-2]== "-" and V[2][1] == "+":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] -sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "-" and V[2][1] == "-":
        somme1=somme1+sum(V00) -sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== "-" and V[2][1] == "/":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] -sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== "-" and V[2][1] == "%":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] -sum (V11) %sum(V22)
    if V[0][len(V[0])-2]== "-" and V[2][1] == "*":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] -sum (V11) *sum(V22)

    if V[0][len(V[0])-2]== "*" and V[2][1] == " ":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] *sum (V11) 
    if V[0][len(V[0])-2]== "/" and V[2][1] == " ":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] /sum (V11) 
    if V[0][len(V[0])-2]== "%" and V[2][1] == " ":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] %sum (V11) 
    if V[0][len(V[0])-2]== "+" and V[2][1] == " ":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] +sum (V11) 
    if V[0][len(V[0])-2]== "-" and V[2][1] == " ":
        somme1=somme1+sum(V00[i] for i in range(0,len(V00)-1)) + V00[len(V00)-1] -sum (V11) 

    if V[0][len(V[0])-2]== " " and V[2][1] == "+":
        somme1=somme1+sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== " " and V[2][1] == "-":
        somme1=somme1+sum (V11) +sum(V22)
    if V[0][len(V[0])-2]== " " and V[2][1] == "*":
        somme1=somme1+sum (V11) *sum(V22)
    if V[0][len(V[0])-2]== " " and V[2][1] == "/":
        somme1=somme1+sum (V11) /sum(V22)
    if V[0][len(V[0])-2]== " " and V[2][1] == "%":
        somme1=somme1+sum (V11) %sum(V22)

    if V[0][len(V[0])-2]== " " and V[2][1] == " ":
        somme1=somme1+sum(V11) 


    return print(somme1)

somme("17 + 3 * 2 - (9 - 8 ) + 5 - 6 ")