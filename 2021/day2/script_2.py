with open("input") as file:
    f = file.read().splitlines()
    h = 0
    v = 0
    aim = 0
    for line in f:
        l_split = line.split(" ")
        cmd = l_split[0]
        x = int(l_split[1])
        if cmd == "forward":
            h += x
            v += x * aim
        elif cmd == "down":
            aim += x
        elif cmd == "up":
            aim -= x

        print(f"h {h}")
        print(f"v {v}")
    print(h*v)
