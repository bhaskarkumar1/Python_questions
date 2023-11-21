ls=[int(input()) for i in range(5)]

min=ls[0]
max=ls[0]
for val in ls:

    if min>val:
        min=val
    if max<val:
        max=val
print(min, max)