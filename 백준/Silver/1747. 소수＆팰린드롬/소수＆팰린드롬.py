n = int(input())

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5+1)):
        if x%i==0:
            return False
    return True

def palin(x):
    if str(x)==str(x)[::-1]:
        return True
    return False

while True:
    if prime(n) and palin(n):
        print(n)
        break
    n+=1