# sort the even index in ascending order and odd in desecnding order

l=[2,4,5,7,8,9,4,4,1,55]

#get the even index elmnt
even=l[::2]
even.sort()
# print(even)

# get the odd index
odd=l[1::2]
odd.sort()
print(odd)

i=0
while i<len(l):

    if i%2==0 :
        l[i]=even[i//2]
    else:
        l[i]=odd[i//2]
    

    i+=1 
print(l)