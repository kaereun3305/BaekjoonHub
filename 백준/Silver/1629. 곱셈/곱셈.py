a, b, c = map(int, input().split())

def pro(a, n):
    if n == 1:
        return a%c
    else:
        temp = pro(a, n//2)
        if n%2==0:
            return (temp*temp)%c
        else:
            return (temp*temp*a)%c

print(pro(a,b))