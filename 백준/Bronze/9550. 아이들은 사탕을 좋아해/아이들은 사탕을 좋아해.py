for _ in range(int(input())):
    N, K = map(int,input().split())
    can = list(map(int, input().split()))
    ans = 0
    
    for i in can:
        ans += i // K
    print(ans)