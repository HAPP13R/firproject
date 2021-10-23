k, d, a = map(int, input("Your KDA >> ").split("/"))
if (d == 0):
    print("Perfect!")
elif ((k + a) / d > 5.0):
    print("Awesome!")
elif ((k + a) / d > 4.0):
    print("Nice!")
elif ((k + a) / d > 3.0):
    print("Good!")
elif ((k + a) / d > 2.0):
    print("Cool")
elif ((k + a) / d > 1.0):
    print("LOL")
else:
    print("Noob :(")
