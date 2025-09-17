i = 3
num_prime = 0

while num_prime < 30:
    x_prime = True
    for j in range(2, i - 1):
        if i % j == 0:
            x_prime = False
            break
    if x_prime:
        y_prime = True
        for k in range(2, i + 2):
            if (i + 2) % k == 0:
                y_prime = False
                break
        if y_prime:
            num_prime += 1
            print(num_prime, "\t",i, "\t", i + 2)

    i += 1