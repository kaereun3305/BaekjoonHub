import sys
from collections import deque

T = int(sys.stdin.readline())
dq = deque()

for _ in range(T):
    a = list(map(int, sys.stdin.readline().split()))
    cmd = a[0]
    
    if cmd == 1:
        dq.appendleft(a[1])
        
    elif cmd == 2:
        dq.append(a[1])
        
    elif cmd == 3:
        if dq:
            print(dq.popleft())
        else:
            print("-1")
            
    elif cmd == 4:
        if dq:
            print(dq.pop())
        else:
            print("-1")
            
    elif cmd == 5:
        print(len(dq))
        
    elif cmd == 6:
        if dq:
            print("0")
        else:
            print("1")
            
    elif cmd == 7:
        if dq:
            print(dq[0])
        else:
            print("-1")
            
    elif cmd == 8:
        if dq:
            print(dq[-1])
        else:
            print("-1")