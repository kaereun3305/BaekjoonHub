def wid(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if floor[x][y]=="-":
        floor[x][y]=1
        wid(x, y-1)
        wid(x, y+1)
        return True
    return False

def leng(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if floor[x][y]=="|":
        floor[x][y]=1
        leng(x-1,y)
        leng(x+1,y)
        return True
    return False

n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if wid(i, j)==True:
            cnt+=1
        if leng(i, j)==True:
            cnt+=1
print(cnt)