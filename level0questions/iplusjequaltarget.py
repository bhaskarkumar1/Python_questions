# l[i]+l[j]== target then count++

# ls=list(map(int,input().split()))
ls=[6,7,3,2,4,7,8]

k=10
count=0

for i in range(len(ls)):
    j=i+1
    while j< len(ls):
        if ls[i]+ls[j]==k:
            count+=1
        j+=1

    
print(count)
