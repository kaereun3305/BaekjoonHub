t = int(input())

for i in range(t):
    stack = []
    n = input()
    valid = True
    
    for j in n:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                valid = False
                break
    
    if valid and not stack:
        print("YES")
    else:
        print("NO")