ls=[["a","b","c"],["d","e","f"],["g","h","i"]]
res=[]
s="f"
def funcn(s):
    for i in range(len(ls)):

        for j in range(len(ls)):

            if ls[i][j]==s:
                row=i
                col=j
    print(row, col)
    #got row and col
    lf=""
    for j in range(len(ls)):
        if j<col:
            lf+=ls[row][j]
    
    up=""
    for  i in range(len(ls)):
        if i<row:
            up+=ls[i][col]
    
    print(up)
    res.append(up)
    res.append(lf)
funcn(s)
print(res)