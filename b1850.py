import math
a, b = map(int, input().split())
s = "1"
print(s * math.gcd(a, b))