n = int(input())
for i in range(n):
    a = list(input().split())
    s = ""
    for x in a:
        x = x.strip()[::-1]
        s += x + " "
    print(s)