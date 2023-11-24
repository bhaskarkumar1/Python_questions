# extract the maxm of all the prime 

ls=[[47,2,3],[4,5,6],[7,8,13]]
l2=[]

for i in range(len(ls)):
    for j in range(len(ls)):
        if i==j or i+j==len(ls)-1:
                l2.append(ls[i][j])
print(l2)
l2.sort()
for i in range(len(l2)-1,-1,-1):
    k=l2[i]
    flag=True
    for j in range(2, abs(l2[i])//2+1):
        if k%j==0:
            flag=False
    if flag:
        print(l2[i])
        break





