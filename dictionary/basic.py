d={}

print(type(d))

a=[1,2,3,4,5,6,1]
b=[10,11,12,13,14,15,16]


# add to dictionary treat a as key and b as a value
for i in range(len(a)):

    # if contains then update the value
    if a[i] in d:
        if b[i]>d[a[i]]:
            d[a[i]]=b[i]
    # else add the key with value 
    else:
        d[a[i]]=b[i]

print(d)

# d.get(key, defaultValue)
print(d.get(47,-1))
print(d.keys())
print(d.values())
print(d.items())


#deletion for specific key
d.pop(2)
print(d)


# count no. of times the element is repeated

l=['a','b','c','d','e','f','a','b','d','c','d','e','f']
d1={}
for i in range(len(l)):
    if l[i] in d1:
        # then update the count to +1
        d1[l[i]]=d1[l[i]]+1
    else:
        d1[l[i]]=1 

print(d1)