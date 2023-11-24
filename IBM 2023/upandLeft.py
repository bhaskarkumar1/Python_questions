rows = [['b','a','b','c'],
        ['z','x','c','v'],
        ['n','d','e','f',],
        ['m','g','h','i']]

up=""
left=""

alphabet="g"


col=None
row=None
for i in range(len(rows)):
    for j in range(len(rows)):
        if rows[i][j]==alphabet:
            col=j
            row=i


#get the all the above element and append it in string named up
# col will be fixed
for i in range(row):
    up+=rows[i][col]



#get the all the left elemnt and append in the left string

for j in range(col):
    left+=rows[row][j]

arr=[]

arr.append(up)
arr.append(left)

print(arr)