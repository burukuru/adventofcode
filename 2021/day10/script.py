def check_matching_bracket(line):
    matching = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }

    closing = []
    missing = None
    for bracket in line:
        if bracket in matching.keys():
            closing.append(matching[bracket])
        else:
            if bracket != closing.pop():
                print(f"No matching bracket found: {bracket}.")
                missing = bracket
                break
    return missing


def calculate_points(brackets):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    sum = 0
    for b in brackets:
        if b is not None:
            sum += points[b]
    return sum


for file in ["test", "input"]:
    with open(file) as f:
        data = f.read().splitlines()
        missing_brackets = []
        for line in data:
            missing_bracket = check_matching_bracket(line)
            missing_brackets.append(missing_bracket)

        points = calculate_points(missing_brackets)
        print(points)
