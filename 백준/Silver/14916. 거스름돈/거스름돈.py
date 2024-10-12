a = int(input())

count = 0

while a>0:
    if a%5==0:
        count+=a//5
        break
    a-=2
    count+=1
    
if a<0:
    print(-1)
    
else:print(count)