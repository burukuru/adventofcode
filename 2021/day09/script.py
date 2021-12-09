import logging

logging.basicConfig(level=logging.DEBUG)


def get_surrounding(data, i, j):
    width = len(data[0]) - 1
    height = len(data) - 1
    values = []
    if i > 0:
        above = data[i - 1][j]
        values.append(above)
    if i < height:
        below = data[i + 1][j]
        values.append(below)
    if j > 0:
        left = data[i][j - 1]
        values.append(left)
    if j < width:
        right = data[i][j + 1]
        values.append(right)

    return list(map(int, values))


def return_if_lowest(datapoint, surrounding):
    if min([datapoint] + surrounding) == datapoint and datapoint not in set(
        surrounding
    ):
        return datapoint
    return None


with open("input") as f:
    data = f.read().splitlines()
    width = len(data[0])
    height = len(data)
    risk = 0

    for i in range(height):
        for j in range(width):
            logging.debug("----------")
            logging.debug("i %s j %s", i, j)
            surrounding = get_surrounding(data, i, j)
            lowest = return_if_lowest(int(data[i][j]), surrounding)
            logging.debug("data %s", data[i][j])
            logging.debug("surrounding %s", surrounding)
            logging.debug("lowest %s", lowest)
            if lowest is not None:
                risk += lowest + 1

    print(risk)
