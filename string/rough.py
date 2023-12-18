a=[1,2,3,4,5]

b=[]

sum=0

for i in range(len(a)):
    if i==0:
        b.append(sum)
    else:
        sum+=a[i-1]
        b.append(sum)

print(b)