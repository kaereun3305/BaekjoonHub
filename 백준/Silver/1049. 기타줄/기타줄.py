n, m = map(int, input().split())

ans = 0 
price_list = []

for i in range(m):
    price = tuple(map(int, input().split()))
    price_list.append(price)
    
six = sorted(price_list, key = lambda x : x[0])
one = sorted(price_list, key = lambda x : x[1])

if six[0][0] <= one[0][1] * 6:
    ans = six[0][0] * (n//6) + one[0][1] * (n%6)
    if six[0][0] < one[0][1] * (n%6):
        ans = six[0][0] * (n//6 + 1)
else: ans = one[0][1] * n

print(ans)