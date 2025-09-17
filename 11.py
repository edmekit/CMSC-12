l = int(input("enter length: "))
w = int(input("enter width: "))

for i in range(0 , l):
    if i == 0 or i == l - 1:
        for j in range(0, w):
            print("*", end=" ")
    else:
        for j in range(0, w):
            if j == 0 or j == w - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()