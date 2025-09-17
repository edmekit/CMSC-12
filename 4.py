a = int(input("enter a: "))
b = int(input("enter b: "))

lowest = 0

for i in range(2, a + b):
    if a % i == 0 and b % i == 0:
        lowest = i
        break

print("LCF:", lowest)
 