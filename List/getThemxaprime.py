# get the max prime number from the diagonal element

ls=[[1,2,3],[4,5,6],[7,8,17]]
# s=set(ls)
# s.remove(1)
# print(max(s))
# print(s)

#extract the pri ary diagonal element and secondary element
s=set()
j=0
for i in range(len(ls)):
    for j in range(len(ls)):
        if i==j or i+j==len(ls)-1:
            s.add(ls[i][j])
print(s)


# remove the max from det and check if its prime or not ,, if prime then break the loop

while len(s)!=0:
    flag=True
    m=max(s)
    for i in range(2 ,abs(m)//2+1):
        if m%i==0:
            s.remove(m)
            flag=False
    if flag:
        print(m)
        break
