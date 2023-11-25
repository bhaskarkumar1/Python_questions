ls=[1,2,3,3,3,3,3,4]


k=int(input())

f=ls.count(k)
res=[-1, -1]

if f==0:
    print(res)
else:
    for i in range(len(ls)):
        if k==ls[i]:
            index=i
            break
    res[0]=index
    res[1]=index+f-1
    print(res)