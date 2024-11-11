n, k = map(int, input().split())

order = []
temp = 0
arr = list(range(1,n+1))

while arr:
    temp += k-1
    temp%=len(arr)
    order.append(str(arr.pop(temp)))


print("<"+", ".join(order)+ ">")