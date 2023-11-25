ls= list(map(int, input().split()))
# ls = list(map(int, input().split()))

res=[None]*len(ls)

j=0
for i in range(len(ls)-1,-1,-1):
    res[j]=ls[i]
    j+=1
print(res)