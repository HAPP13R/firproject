while(True):
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    c = a
    c -= b - a
    print(c)