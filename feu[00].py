def RECt(a,b):
    l='0'
    p='|'
    for i in range (0,a):
        l=l+"-"
        p=p+' '

    l=l+'0'
    p=p+"|"

    print(l)

    for j in range(0,b):
        print(p)
    
    if b>0:
        print(l)

RECt(7,5)
    