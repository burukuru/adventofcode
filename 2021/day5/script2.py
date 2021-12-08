from collections import Counter
import logging

logging.basicConfig(level=logging.DEBUG)

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
        logging.debug("expanded %s", expanded_coords)
        all_coords += expanded_coords

    return all_coords

def expand_coord(start, end):
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    coords = []
    if (y1 - y2 == x1 - x2
            or y2 - y1 == x2 - x1):
        logging.debug(f"x1 {x1}, y1 {y1}")
        logging.debug(f"x2 {x2}, y2 {y2}")
        logging.debug("/")
        x_expand = range(min(x1, x2), max(x1, x2)+1)
        y_expand = range(min(y1, y2), max(y1, y2)+1)
        coords = list(zip(x_expand, y_expand))
        for coord in coords:
            print(coord)
    elif (y1 - y2 == x2 - x1
            or y2 - y1 == x1 - x2):
        logging.debug(f"x1 {x1}, y1 {y1}")
        logging.debug(f"x2 {x2}, y2 {y2}")
        logging.debug("\\")
        if x1 > x2:
            x_expand = range(x1, x2-1,-1)
            y_expand = range(min(y1, y2), max(y1, y2)+1)
        elif x2> x1:
            x_expand = range(x2, x1-1,-1)
            y_expand = range(min(y1, y2), max(y1, y2)+1)

        print(x_expand)
        print(y_expand)
        coords = list(zip(x_expand, y_expand))
    elif x1 == x2:
        y_expand = range(min(y1, y2), max(y1, y2)+1)
        coords = [ [x1, y] for y in y_expand ]
    elif y1 == y2:
        x_expand = range(min(x1, x2), max(x1, x2)+1)
        coords = [ [x, y1] for x in x_expand ]

    print(coords)
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
