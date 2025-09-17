n = int(input("Enter a  number: "))


num_prime = 0

for i in range(n + 1, n * 2):
    x_prime = True
    for j in range(2, i):
        if i % j == 0:
            x_prime = False
            break
    if x_prime:
        num_prime += 1
    else:
        continue
    

print(num_prime)