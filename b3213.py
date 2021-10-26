n = int(input())
a = 0
for i in range(n):
    s = input()
    if s == "1/4":
        a += 1
    elif s == "1/2":
        a += 2
    elif s == "3/4":
        a += 3
a /= 4.0
print(a)
# if a % 1 != 0:
#     a += 1
# print(a)