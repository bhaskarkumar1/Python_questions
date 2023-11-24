# 0
# 1 1
# 2 3 5
# 8 13 21 34

n=5
a=0
b=1
for i in range(n):

    for j in range(n):
        if j<=i:
            c=a+b
            a=b
            b=c
            print("%3d "%(c),end="")
        # else:
            
    print()