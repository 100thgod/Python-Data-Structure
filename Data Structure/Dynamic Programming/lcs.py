#longest comman subsequence
c=[]
def LCSLength(x,y):
    m,n = len(x), len(y)
    for i in range(m+1):
        c.append([None]*(n+1))
    for i in range(m+1):
        c[i][0] = 0
    for i in range(n+1):
        c[0][i] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            else:
                c[i][j] = max(c[i][j-1],c[i-1][j])
    return c[m][n]

def backtrack(c,x,y,i,j):
    if i==0 or j == 0:
        return ""
    elif x[i-1] == y[j-1] :
        return backtrack(c,x,y,i-1,j-1) +x[i-1]
    else:
        if c[i][j-1] > c[i-1][j]:
            return backtrack(c,x,y,i,j-1)
        else:
            return backtrack(c,x,y,i-1,j)
def backtrackAll(c,x,y,i,j):
    if i==0 or j == 0:
        return ""
    elif x[i-1] == y[j-1] :
        return list(z+list(x[i-1]) for z in backtrackAll(c,x,y,i-1,j-1))
    else:
        R =[]
        if c[i][j-1] >= c[i-1][j]:
            R.append(backtrackAll(c,x,y,i,j-1))
        if c[i][j-1] <= c[i-1][j]:
            R.append(backtrackAll(c,x,y,i-1,j))
    return R
print(LCSLength("GAC","AGCAT"))
print(backtrackAll(c,"GAC","AGCAT",3,5))