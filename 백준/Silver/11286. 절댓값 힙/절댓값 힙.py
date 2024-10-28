import sys
from heapq import heappush, heappop

n = int(input())

heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x!=0:
        heappush(heap,(abs(x), x))
    elif x==0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)