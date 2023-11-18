n = int(input())
sum = 0

while True:
# print(sum)
    if n>9:
        while n>0:
            sum+=n%10
            n//=10
        n=sum
        sum=0
    else:
        print(n)
        break

