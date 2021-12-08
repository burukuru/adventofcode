import logging
from collections import Counter

logging.basicConfig(level=logging.INFO)

DAYS = 256

def add_fish(fish_counter):
    new_fish_counter = {}
    for i in range(9):
        new_fish_counter.update({i:0})

    for fish_days, fish_count in fish_counter.items():
        if fish_days == 0:
            new_fish_counter[8] += fish_count
            new_fish_counter[6] += fish_count
        else:
            new_fish_counter[fish_days - 1] += fish_count
    # print("=========")
    # print(f"1 {new_fish_counter.get(1)}")
    # print(f"7 {new_fish_counter.get(7)}")
    # print(f"6 {new_fish_counter.get(6)}")
    return new_fish_counter


with open("input") as f:
    fish_list = f.read().splitlines()[0].split(",")
    fish_list = [int(fish) for fish in fish_list]
    fish_counter = dict(Counter(fish_list))
    for d in range(DAYS):
        fish_counter = add_fish(fish_counter)
    total_fish = sum(fish_counter.values())
    print(total_fish)
