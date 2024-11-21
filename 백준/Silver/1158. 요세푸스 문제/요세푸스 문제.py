from collections import deque

T, K = map(int, input().split())
arr = deque()
for i in range(1,T+1):
    arr.append(i)

yp = []
cnt = 0

while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())
    yp.append(arr.popleft())

print(str(yp).replace('[', '<').replace(']', '>'))