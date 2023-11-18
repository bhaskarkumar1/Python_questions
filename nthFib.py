a=0
b=1
n=int(input())
count=2
while True:
    curr=a+b
    a=b
    b=curr
    count+=1

    if count==n:
        print(curr)
        break