import sys
ls=[12,34,5,6,4,4,34]

#get the first max and first smallest
max,min=ls[0],ls[0]

for val in ls:
    if min>val:
        min=val
    if max<val:
        max=val
# now again find min and max but this time dont update the val if its fmin and fmax

newList=set(ls)
print(newList)
newList.remove(max)
newList.remove(min)
#get the first max and first smallest
smax,smin=ls[0],ls[0]

for val in newList:
    if smin>val:
        smin=val
    if smax<val:
        smax=val
print(max, min)
print(smax, smin)