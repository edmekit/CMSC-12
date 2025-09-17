n = int(input("Enter a  number: "))

x_prime = True

for i in range(2, n):
    if n % i == 0:
        print("n is composite.")
        x_prime = False
        break

if x_prime:
    print("n is prime.")