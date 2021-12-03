with open("input1") as file:
    f = file.read().splitlines()
    increased = 0
    sliding = []
    for i, line in enumerate(f):
        if i in (0, 1):
            continue
        else:
            sliding.append(int(line) + int(f[i-1]) + int(f[i-2]))

    for i, line in enumerate(sliding):
        if i == 0:
            continue
        elif int(line) > int(sliding[i-1]):
            increased +=1

    print(increased)
