""""
5 4 3 2 1 
  5 4 3 2
    5 4 3
      5 4
        5

"""

n=int(input())

for i in range(1,n+1):
    k=n
    for j in range(1,n+1):
        if j>=i:
            print(k, end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()