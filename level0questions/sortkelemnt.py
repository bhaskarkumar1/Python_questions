# sort k element in ascending order and k element in descending order

l=[6,423,12,67,23,68,23,6]

#get the 1st k element and last k elment
k=int(input())
fs=l[0:k:1]
fs.sort()
# print(fs)
ls=l[k:]
ls.sort(reverse=True)
print(ls)

# print(fs.extend(ls))
fs.extend(ls)
print(fs)

