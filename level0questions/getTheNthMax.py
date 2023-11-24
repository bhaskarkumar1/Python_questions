ls=[1,2,3,4,78,1,-96,47]

#while we not the nth max
    # get the first max 
    # and remove it until the loop

n=int(input())
i=0
m=None
while i<n:
    # m=max(ls)
    # print(m)
    # c=m
    m=ls[0]
    for val in ls:
        if val>m:
            m=val

    c=m
    ls.remove(m)
    i+=1
print(c)
