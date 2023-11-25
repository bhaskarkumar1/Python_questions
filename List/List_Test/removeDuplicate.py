ls= list(map(int,input().split()))

for i in range(len(ls)-1):
    j=i+1

    while j<len(ls):
        if ls[i]==ls[j]:
            del ls[j]
        else:
            j+=1
print(ls)