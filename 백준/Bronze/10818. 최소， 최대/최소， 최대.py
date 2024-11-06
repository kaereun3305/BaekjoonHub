import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

print(arr[0], arr[n-1])