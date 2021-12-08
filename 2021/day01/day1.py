with open("input1") as file:
    f = file.read().splitlines()
    increased = 0
    for i, line in enumerate(f):
        if i == 0:
            continue
        elif int(line) > int(f[i-1]):
            increased +=1

    print(increased)
