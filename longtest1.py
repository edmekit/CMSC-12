N = int(input("Enter how many number: "))

largest_1 = 0
largest_2 = 0

while N > 0:
    num = int(input("Enter a number: "))
    if num > largest_1:
        largest_2 = largest_1
        largest_1 = num
    elif num > largest_2:
        largest_2 = num
    N -= 1

print("The largest number is", largest_1)
print("The second largest number is", largest_2)