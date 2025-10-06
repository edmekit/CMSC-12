def getGCF(a,b):
    highest = 0

    for i in range(2, a + b):
        if a % i == 0 and b % i == 0:
            highest = i

    return highest

def getLCF(a,b):

    lowest = 0

    for i in range(2, a + b):
        if a % i == 0 and b % i == 0:
            lowest = i
            return lowest