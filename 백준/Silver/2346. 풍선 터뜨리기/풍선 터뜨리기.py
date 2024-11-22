from collections import deque

T = int(input())

arr = deque(enumerate(map(int, input().split())))
ans = []

while arr:
    index, turn = arr.popleft()
    ans.append(index + 1)

    if turn>0:
        arr.rotate(-(turn - 1))
    elif turn<0:
        arr.rotate(-turn)

print(' '.join(map(str, ans)))