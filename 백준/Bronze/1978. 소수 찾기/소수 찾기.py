import math
n = int(input())
m = list(map(int, input().split()))
cnt = 0

for i in m:
    if i <2:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            break
    else: cnt+=1
print(cnt)