n, m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

def flip(i,j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1 - a[x][y]

cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            flip(i, j)
            cnt+=1
        if a==b:break
    if a==b:break

if a==b: print(cnt)
else: print(-1)