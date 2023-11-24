ls=[1,2,71,1,6,4,245,25,245]


max=ls[0]
for i in range(len(ls)):
    if max<ls[i]:
        max=ls[i]

#got the max input index now remove it
# print(max)
ls.remove(max)

max2=ls[0]

for i in range(len(ls)):
    if max2<ls[i]:
        max2=ls[i]
    
print(max2)
