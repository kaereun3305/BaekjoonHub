N, k, l = map(int, input().split())
count=0

while k!=l:
    k-=k//2
    l-=l//2
    count+=1
    
print(count)