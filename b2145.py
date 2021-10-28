while True:
    a = int(input())
    if a == 0:
        break
    while a > 9:
        s = 0
        while a > 0:
            s += a % 10
            a //= 10
        a = s
    print(a)

