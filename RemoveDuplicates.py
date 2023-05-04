numbers = [0, 1, 2, 3, 3, 4, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)
