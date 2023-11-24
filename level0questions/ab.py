m,n=map(int, input().split())

ls=[]
for i in range(m,n+1):
    if abs(i)!=1:
        for j in range (2, abs(i)//2+1):
            if abs(i)%j==0:
                break
        else:
            ls.append(i)
print(ls)
print(min(ls),max(ls))