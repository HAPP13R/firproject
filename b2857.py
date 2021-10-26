a = ""
for i in range(5):
    s = input()
    if "FBI" in s:
        a += str(i + 1) + " "

if a == "":
    print("HE GOT AWAY!")
else:
    print(a)