def count_unique(digits):
    unique = 0
    print(digits)
    for digit in digits:
        digit_length = len(digit)
        if digit_length in [2, 4, 3, 7]:
            unique += 1
    return unique

with open("input") as f:
    data = f.read().splitlines()
    unique_list = []
    for line in data:
        l_split = line.split(" | ")
        signals = l_split[0].split()
        digits = l_split[1].split()
        unique = count_unique(digits)
        unique_list.append(unique)

    print(sum(unique_list))
