while True:
    secret = input()
    if secret == "END":
        break
    else:
        secret = secret[::-1]
        print(secret)