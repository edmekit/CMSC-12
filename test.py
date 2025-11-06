def count(ls):
    highest1 = 'z'
    highest2 = 'y'

    encountered = []

    for i in range(0, len(ls)):
        if ls[i] in encountered:
            if ls[i] != highest1:
                highest2 = ls[i]
            else:
                highest1 = ls[i]
        else:
            encountered.append(ls[i])

    return highest1, highest2

letters = ['a', 'b', 'a', 'c', 'b', 'a']
print(count(letters))