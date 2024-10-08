n, k = map(int,input().split())
coins = list()

for i in range(n):
    coins.append(int(input()))

ans = 0

for i in reversed(range(n)):
    ans += k//coins[i]
    k = k%coins[i]
    
print(ans)