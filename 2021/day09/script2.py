import logging

logging.basicConfig(level=logging.INFO)


def right_value(data, i, j):
    return int(data[i][j + 1])


def up_value(data, i, j):
    return int(data[i - 1][j])


def down_value(data, i, j):
    return int(data[i + 1][j])


def left_value(data, i, j):
    return int(data[i][j - 1])


def get_surrounding(sink, counted, data, i, j, prev=None):
    value = int(data[i][j])
    logging.debug("-------")
    logging.debug("value %s", value)
    if (i, j) in counted:
        return
    if value < 9:
        sink.add((i, j))
        counted.add((i, j))

        logging.debug("i %s", i)
        logging.debug("j %s", j)
        width = len(data[0]) - 1
        height = len(data) - 1
        if i > 0 and up_value(data, i, j) < 9:
            get_surrounding(sink, counted, data, i - 1, j, (i, j))
        if i < height and down_value(data, i, j) < 9:
            get_surrounding(sink, counted, data, i + 1, j, (i, j))
        if j > 0 and left_value(data, i, j) < 9:
            get_surrounding(sink, counted, data, i, j - 1, (i, j))
        if j < width and right_value(data, i, j) < 9:
            get_surrounding(sink, counted, data, i, j + 1, (i, j))

    return sink


with open("input") as f:
    data = f.read().splitlines()
    width = len(data[0])
    height = len(data)
    sinks = []
    counted = set()

    for j in range(width):
        for i in range(height):
            sink = set()
            logging.debug("----------")
            logging.debug("i %s j %s", i, j)
            surrounding = get_surrounding(sink, counted, data, i, j)
            sinks.append(len(sink))

    result = 1
    for _ in range(3):
        print(max(sinks))
        result *= max(sinks)
        sinks.remove(max(sinks))
    print(result)
