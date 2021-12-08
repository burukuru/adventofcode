INPUT_FILE = "input"

def calc_fuel(crab_position, target_position):
    distance = abs(crab_position-target_position)
    fuel_usage = 0
    for i in range(1, distance+1):
        fuel_usage +=i
    return fuel_usage

with open(INPUT_FILE) as f:
    data = list(map(int, f.read().strip().split(",")))
    fuel_min = 0
    for target_position in range(max(data)):
        fuel_sum = 0
        for crab_position in data:
            fuel_sum += calc_fuel(crab_position, target_position)
        if fuel_min == 0:
            fuel_min = fuel_sum
        else:
            fuel_min = min(fuel_min, fuel_sum) 

    print(fuel_min)
