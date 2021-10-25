n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lst2 = []
for i in lst:
    lst2.append(i / m * 100.0)
avg = sum(lst2) / n
print(avg)