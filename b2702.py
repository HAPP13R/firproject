import math

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    print(f"{int(a*b / g)} {g}")