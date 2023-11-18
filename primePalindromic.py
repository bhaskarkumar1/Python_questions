# if prime check for palindromic
n=int(input())
count=0
i=2
o=0
e=0
while True:

    #find the curr no. is prime or not, if prime the n proceed for checking palindrome
    flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=False
            break
    if flag:
        rev=0
        c=i
        while(c>0):
            rev=rev*10+c%10
            c//=10
        if i!=rev:
            flag=False
        
        if flag==True:
            # print(i,end=" ")

            # i == calculate the digit
            v=i
            digit=0
            while v>0:
                v//=10
                digit+=1
            if digit%2==0:
                e+=1
            else:
                o+=1
             
            count+=1



    i+=1
    if count==n:
        break


print(f"odd palindromic prime: {o} and\n even palindromic prime: {e}")