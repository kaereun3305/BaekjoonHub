ans = 0
max_ans = 0
for i in range(10):
    a, b = map(int, input().split())
    ans += (b-a)
    max_ans = max(ans, max_ans)

print(max_ans)