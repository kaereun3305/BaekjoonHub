import math

M = 123456

arr = [True for _ in range(2*M + 1)]
arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(2*M))+1):
    if arr[i]:
        j = 2
        while i * j <= 2 * M:
            arr[i*j]=False
            j+=1

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for i in range(n+1, 2*n + 1):
        if arr[i]:
            cnt +=1
    print(cnt)