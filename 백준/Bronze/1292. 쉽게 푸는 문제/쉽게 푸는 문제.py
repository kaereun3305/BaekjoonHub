n, m = map(int, input().split())
arr = [0]

for i in range(1,m+1):
    for j in range(i):
        arr.append(i)
ans = 0

for i in range(n, m+1):
  ans+=arr[i]
print(ans)