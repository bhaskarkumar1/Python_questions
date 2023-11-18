a,b=map(int, input().split())

while b!=0: 
    t=b
    b=a%b
    a=t
if a==1:
    print("Coprime")
else:
    print("Not coprime")