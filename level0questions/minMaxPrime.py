m,n=map(int, input().split())
# m=-30
# n=0

max=0

min_prime = None  # Initialize min_prime to None

for i in range(m, n + 1, 1):
    flag = True
    if i!=0 and i!=-1 and i!=1: 
        for j in range(2, abs(i) // 2 + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            min_prime = i
            break
    # prime number from right end
for i in range(n,m,-1):

    flag=True
    if  i!=0 and i!=-1 and i!=1:
        for j in range(2,abs(i)//2+1):
            if i%j==0:
                flag=False
                break
        if flag:
            max=i
            break
print(min_prime, max)