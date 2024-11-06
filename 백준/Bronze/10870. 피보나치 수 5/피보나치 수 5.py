def pib(n):
    if n <=1:
        return n
    return pib(n-1) + pib(n-2)

print(pib(int(input())))