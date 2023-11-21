# check given negative number is prime or not 
n= int(input())

for i in range(2,abs(n)//2+1):
    flag=True 
    if n%i==0:
        flag=False 
        break
if flag:
    print(f"{n} is a prime " )
else:
    print(f"{n} not a prime")
