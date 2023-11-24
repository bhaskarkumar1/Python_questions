# you will be given a number then you will have to using those digit, u have to form the number which is greater than the given digit

n=int(input())
ls=[]
while n!=0:
    ls.append(n%10)
    n//=10
# now sort the ls in rev order

ls.sort(reverse=True)

print(*ls)