s="geekforgeek"
n=len(s)

for i in range(1,n+1):
    for j in range(1+n+1):
        if i==j:
            print(s[i-1],end=" ")
        elif i+j==n+1:
            print(s[n-i],end=" ")
        else:
            print(" ",end=" ")
    print()
        
        