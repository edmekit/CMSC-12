n = int(input("How many numbers: "))

zero_count = 0

for i in range(0, n):
    num = int(input("ENter a number: "))
    if num == 0:
        zero_count += 1
    
print(zero_count)
