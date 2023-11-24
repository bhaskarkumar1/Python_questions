#you are given a number 63524918 you have to sorted number
#  eg it will return 12345689

n=int(input())

ls=[]

while n!=0:
    ls.append(n%10)
    n//=10
ls.sort()
s=""
for val in ls:
    s+=str(val)
print(s)