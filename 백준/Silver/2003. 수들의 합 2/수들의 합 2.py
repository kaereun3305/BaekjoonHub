n, m = map(int, input().split())
A = list(map(int, input().split()))

count = 0
i = 0
j = 1

while j<=n and i<=j :
   
    partsum = sum(A[i:j])
    
    if partsum == m:
        count+=1
        j+=1
        
    elif partsum < m:
        j+=1
        
    else: i+=1
        
print(count)