def check_matching_bracket(line):
    matching = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }

    closing = []
    for bracket in line:
        if bracket in matching.keys():
            closing.append(matching[bracket])
        else:
            if bracket != closing.pop():
                return
    return closing


def calculate_completion_points(brackets):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = 0
    for bracket in brackets[::-1]:
        score *= 5
        score += points[bracket]
    return score


for file in ["test", "input"]:
    with open(file) as f:
        data = f.read().splitlines()
        scores = []
        for line in data:
            incomplete = check_matching_bracket(line)
            if incomplete is not None:
                score = calculate_completion_points(incomplete)
                scores.append(score)
        scores.sort()
        print(scores[len(scores) // 2])
