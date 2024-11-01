n = int(input())

stack, ans, can = [], [] , True

now = 1

for i in range(n):
    num = int(input())
    
    while now<=num:
        stack.append(now)
        ans.append('+')
        now +=1
        
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
        
    else:
        can = False
        
if not can:
    print("NO")
else:
    for j in ans:
        print(j)