import sys
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = deque(list(map(int, sys.stdin.readline().split())))
    
    count = 0
    
    while data:
        best = max(data)
        front = data.popleft()
        m-=1
        
        if best==front:
            count+=1
            
            if m<0:
                print(count)
                break
        else:
            data.append(front)
            
            if m<0:
                m = len(data)-1