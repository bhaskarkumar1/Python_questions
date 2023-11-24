#  smallest number formed by the digits of 901230 is 100239.
# dont ignore the 0 0

n=int(input())

# extract the digit and sort it in acending order

ls=[]

c=n
while n!=0:
    ls.append(n%10)
    n//=10

ls.sort()
s=""
for i in range(len(ls)):
    #count zeroes
    zero=ls.count(0)
    if i==0:
        m=min(ls[zero:])
        s+=str(m)
        ls.remove(m)
    else: 
        n=min(ls)
        s+=str(n)
        ls.remove(n)



    
print(s)