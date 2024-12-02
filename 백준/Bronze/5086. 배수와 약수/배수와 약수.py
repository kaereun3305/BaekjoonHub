while True:
    A, B = map(int, input().split())

    if A==0 and B==0:
        break
    ans = ''
    if B%A==0:
        ans = 'factor'

    elif A%B==0:
        ans = 'multiple'
    else:
        ans = 'neither'
    
    print(ans)