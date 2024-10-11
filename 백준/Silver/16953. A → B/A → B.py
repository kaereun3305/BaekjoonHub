M, N = map(int, input().split())
ans = 1

while(M!=N):
    ans +=1
    temp = N
    if(N%10==1):
        N//=10
    elif(N%2==0):
        N//=2
    if temp ==N:
        print(-1)
        break

else:
    print(ans)