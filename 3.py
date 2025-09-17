a = int(input("enter a: "))
b = int(input("enter b: "))

highest = 0

for i in range(1, a + b):
    if a % i == 0 and b % i == 0:
        highest = i

print("GCF:", highest)
