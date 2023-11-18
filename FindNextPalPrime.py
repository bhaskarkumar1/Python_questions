#find next palindrominc [prime]


n=int(input())


while True:
    n+=1
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
            break
    
    
    if flag:
        # print(n)
        c=n
        rev=0
        while c>0:
            rev=rev*10+c%10
            c//=10

        if(rev==n):
            print(n)
            break