n= int(input())
list = list(map(int, input().split()))
alr = [False]*n

ans = 0

def jae(mi):
    global ans
    if len(mi)==n:
        total = 0
        for i in range(n-1):
            total+=abs(mi[i]-mi[i+1])
        ans = max(ans,total)
        return
    for i in range(n):
        if not alr[i]:
            alr[i] = True
            mi.append(list[i])
            jae(mi)
            alr[i] = False
            mi.pop()
jae([])
print(ans)