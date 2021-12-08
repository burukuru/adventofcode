with open("input") as file:
    f = file.read().splitlines()
    h = 0
    v = 0
    for line in f:
        l_split = line.split(" ")
        if l_split[0] == "forward":
            h += int(l_split[1])
        elif l_split[0] == "down":
            v += int(l_split[1])
        elif l_split[0] == "up":
            v -= int(l_split[1])


    print(h*v)
