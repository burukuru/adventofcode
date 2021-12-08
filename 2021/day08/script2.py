def digit_mapping(digits):
    digit_mapping = {}
    letter_mapping = {}
    for digit in digits:
        digit_length = len(digit)
        if digit_length == 2:
            digit_mapping[digit] = 1
            letter_mapping[1] = digit
        elif digit_length == 4:
            digit_mapping[digit] = 4
            letter_mapping[4] = digit
        elif digit_length == 3:
            digit_mapping[digit] = 7
            letter_mapping[7] = digit
        elif digit_length == 7:
            digit_mapping[digit] = 8
            letter_mapping[8] = digit

    for digit in digits:
        digit_length = len(digit)
        s = set(digit)
        if digit_length == 6:
            if (s.issuperset(letter_mapping[4]) 
                    and s.issuperset(letter_mapping[7])):
                digit_mapping[digit] = 9
                letter_mapping[9] = digit
            elif (s.issuperset(letter_mapping[1]) ):
                digit_mapping[digit] = 0
                letter_mapping[0] = digit
            else:
                digit_mapping[digit] = 6
                letter_mapping[6] = digit

    btm_left = set(letter_mapping[8]).difference(set(letter_mapping[9]))
    middle = set(letter_mapping[8]).difference(set(letter_mapping[0]))

    for digit in digits:
        digit_length = len(digit)
        s = set(digit)
        if digit_length == 5:
            if btm_left.issubset(s):
                digit_mapping[digit] = 2
                letter_mapping[2] = digit
            # 3 5
            elif (s.issuperset(letter_mapping[1]) ):
                digit_mapping[digit] = 3
                letter_mapping[3] = digit
            else:
                digit_mapping[digit] = 5
                letter_mapping[5] = digit


    print(digit_mapping)
    return digit_mapping

def decifer(digit_map, digits):
    answer = []
    for digit in digits:
        for dm in digit_map.keys():
            print(set(digit))
            print(set(dm))
            if set(digit) == set(dm):
                answer.append(digit_map[dm])
    answer = int("".join([str(digit) for digit in answer]))
    return answer


with open("input") as f:
    data = f.read().splitlines()
    unique_list = []
    sum = 0
    for line in data:
        l_split = line.split(" | ")
        signals = l_split[0].split()
        digits = l_split[1].split()
        digit_map = digit_mapping(signals)
        sum += (decifer(digit_map, digits))

    print(sum)
