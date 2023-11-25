ls= list(map(int,input().split()))

s=set(ls)


for val in s:
    count=0

    for i in range(len(ls)):
        if ls[i]==val:
            count+=1
    print(val,'->',count)

# print(s)