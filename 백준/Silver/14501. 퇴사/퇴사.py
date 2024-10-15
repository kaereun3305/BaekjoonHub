n = int(input())

list = [0] * (n+1)
t=[]
p =[]

for _ in range(n):
    t1, p1 = map(int, input().split())
    t.append(t1)
    p.append(p1)

for i in range(n-1, -1, -1):
    if t[i]+i > n:
        list[i] = list[i+1]
    else:
        list[i] = max(list[i+1], list[t[i]+i]+p[i])

print(list[0])