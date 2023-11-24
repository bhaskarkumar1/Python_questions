n=int(input())
s=""
while n!=0:
    
    r=n%2
    n//=2
    s+=str(r)
    

print(s[::-1])
    