from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)

def extract_coords(data):
    coords = []
    for line in data:
        coord = line.split()
        coords.append([coord[0], coord[2]])
    return coords

def expand_coords(coord_list):
    all_coords = []
    for coord in coord_list:
        logging.debug("==================")
        expanded_coords = expand_coord(coord[0], coord[1])
        logging.debug(expanded_coords)
        all_coords += expanded_coords

    return all_coords

def expand_coord(start, end):
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    logging.debug(f"x1 {x1}, y1 {y1}")
    logging.debug(f"x2 {x2}, y2 {y2}")
    coords = []
    if x1 == x2:
        y_expand = range(min(y1, y2), max(y1, y2)+1)
        coords = [ [x1, y] for y in y_expand ]
    elif y1 == y2:
        x_expand = range(min(x1, x2), max(x1, x2)+1)
        coords = [ [x, y1] for x in x_expand ]

    return coords

def count_coords(coordinates):
    simple_coords = []
    for coord in coordinates:
        simple_coord = str(coord[0]) + "+"+str(coord[1])
        simple_coords.append(simple_coord)

    counter = Counter(simple_coords)
    logging.debug(counter)

    danger = 0
    for coord in counter:
        if counter[coord] >=2:
            danger += 1
    logging.info(danger)

with open("test") as f:
    file = f.read().splitlines()
    coords = extract_coords(file)
    all_coords = expand_coords(coords)
    count_coords(all_coords)

with open("input") as f:
    file = f.read().splitlines()
    coords = extract_coords(file)
    all_coords = expand_coords(coords)
    # print(all_coords)
    count_coords(all_coords)
