h = int(input("enter height of christmas tree: "))

for i in range(1, h + 1):
    for j in range(0, i + 2):
        print(" " * (h + 1 - j), end=" ")
        print(" *" * (j), end=" ")
        for k in range(1, j + i + 2):
            print("*", end=" ")
        print()