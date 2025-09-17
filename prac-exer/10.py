h = int(input("Enter height: "))

for i in range(0, h):
    print(" " * (h - i), end="")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()