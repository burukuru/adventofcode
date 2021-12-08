import logging

logging.basicConfig(level=logging.INFO)

DAYS = 80

def add_fish(fish_list):
    print(fish_list)
    print(len(fish_list))
    new_fish_list = []
    for i, fish in enumerate(fish_list):
        if fish == 0:
            new_fish_list.append(6)
            new_fish_list.append(8)
        else:
            new_fish_list.append(fish-1)

    return  new_fish_list


with open("input") as f:
    fish_list = f.read().splitlines()[0].split(",")
    fish_list = [int(fish) for fish in fish_list]
    for d in range(DAYS):
        fish_list = add_fish(fish_list)
    print(fish_list)
    print(len(fish_list))
