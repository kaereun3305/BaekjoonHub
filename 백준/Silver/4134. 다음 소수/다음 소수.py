N = int(input())

def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
for _ in range(N):
    num = int(input())
    if prime(num):
        print(num)
    else:
        i = num + 1
        while True:
            if prime(i):
                print(i)
                break
            i+=1