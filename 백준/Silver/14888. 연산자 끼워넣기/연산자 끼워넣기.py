N = int(input())
arr = list(map(int, input().split()))
opers = list(map(int, input().split()))

max_val = -(10 ** 9)
min_val = 10 ** 9

def cal(now, total, plus, minus, multi, divide):
    global max_val
    global min_val

    if now == N:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return

    if plus:
        cal(now+1, total+arr[now], plus-1, minus, multi, divide)

    if minus:
        cal(now+1, total - arr[now], plus, minus-1, multi, divide)
    
    if multi:
        cal(now+1, total * arr[now], plus, minus, multi-1, divide)

    if divide:
        cal(now+1, int(total/arr[now]), plus, minus, multi, divide-1)

cal(1, arr[0], opers[0], opers[1], opers[2], opers[3])
print(max_val)
print(min_val)