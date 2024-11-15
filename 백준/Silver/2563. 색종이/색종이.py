n = int(input())

white = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            white[i][j]=1

ans = 0
for k in range(100):
    ans+=white[k].count(1)
print(ans)