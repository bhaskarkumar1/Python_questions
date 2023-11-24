# rotate the list from last, k times

l=[6,423,12,67,23,68,23,6]

k=int(input())

k=k%len(l)

c=l[-k:]+l[:-k]
print(c)
