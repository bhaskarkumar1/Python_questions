# you are given a list 
# 2 players are playing p1,p1
# starting with p1 and then p2
# adding the 1st val to p1 score and if val ==even reverse the rem list

ls=[1,2,3,4,5]

s1,s2=0,0
p1=True
p2=False
n = len(ls)

i=0
while i<n:
    firstEl=ls.pop(0)
    if firstEl%2==0:
        ls.reverse()
    if p1:
        s1+=firstEl
        print(s1)
        p2=True
        p1=False
    elif p2                                         :
        s2+=firstEl
        print(s2)
        p1=True
        p2=False
    i+=1

    
print(i)
print(s1-s2)    
