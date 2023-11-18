a,b,c=map(int,input().split())

if a>b:
    if a>c: 
        if b>c:
            print(a,b,c)
        else:
            print(a,c,b)
    # c>a
    else:
        if b>a:
            print(c,b,a)
        else:
            print(c,a,b) 

#b>a
else:
    if b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)

    else:
#c>b    
        print(c,b,a)

