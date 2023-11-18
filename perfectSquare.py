# n=int(input())


    # if the given number 4 digit number is pf then there first 2 digit and last 2 digit must be PF too 


for n in range(1000, 9999):
    p=int(n**0.5)
    if p*p==n:
        # print("Print pf")
        #extract the first 2 digit ND last 2 digit from 4 digit number
        f=n//100
        l=n%100
        f1=int(f**0.5)
        l1=int(l**0.5)

        if f1*f1==f and l1*l1==l:
            print(n, end=" ")
