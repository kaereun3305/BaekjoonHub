N = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]
for i in range(len(N)):
    print(chess[i]-N[i])

