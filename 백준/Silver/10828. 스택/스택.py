import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    st_order = sys.stdin.readline().split()
    
    if st_order[0] == 'push':
        stack.append(st_order[1])
        
    elif st_order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif st_order[0] == 'size':
        print(len(stack))
        
    elif st_order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif st_order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])