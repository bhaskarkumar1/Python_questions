# s="a1b10"
s="b3c6d15"
i=0

result=""
while True:
    d1=0
    d2=0
    times=0
    if ord(s[i])>=97 and ord(s[i])<=122:
        #it will be a character not integer
        chr=s[i]
        result+=chr

    else:
        #else it will be a digit
        d1=int(s[i])
        if i+1<len(s):
            if not(ord(s[i+1])>=97 and ord(s[i+1])<=122):
                d2=int(s[i+1])
                i+=1
                times=d1*10+d2
            else:
                times=d1
    if 97<=ord(result[-1])<=122:
        # result+=(result[-1]*(times-1))
        result += str(result[-1] * (times - 1))


    # print(chr,d1,d2)
    i+=1
    if i==len(s):
        # print("i: ",i)
        print(result)
        break