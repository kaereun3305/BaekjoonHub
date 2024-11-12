stack = []
temp = 1
ans = 0

n = list(input())

for i in range(len(n)):
    if n[i] =='(':
        temp*=2
        stack.append(n[i])

    elif n[i] =='[':
        temp*=3
        stack.append(n[i])
    
    elif n[i] ==')':
        if not stack or stack[-1]!='(':
            ans = 0
            break
        if n[i-1] =='(':
            ans +=temp
        temp//=2
        stack.pop()

    elif n[i]==']':
        if not stack or stack[-1]!='[':
            ans = 0
            break
        if n[i-1] =='[':
            ans +=temp
        temp//=3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)