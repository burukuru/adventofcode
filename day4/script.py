def find_boards(file):
    boards = []
    boards.append([])
    board_index = 0
    for line in file:
        if line == "":
            boards.append([])
            board_index += 1
        else:
            boards[board_index].append(line.split())
        
    return boards

def find_winning_board(selected, boards):
    for board in boards:
        winning = check_board(selected,board)
        if winning is not None:
            calculate_score(selected, board)
            exit(0)


def check_board(selected, board):
    win = check_horizontal(selected, board)
    if win is True:
        return board
    else:
        win = check_vertical(selected,board)
        if win is True:
            return board
    return None


def check_horizontal(selected, board):
    for line in board:
        # print(f"selected {selected}")
        # print(line)
        if set(line).issubset(set(selected)):
            # print("winner!!!")
            # print(f"selected {selected}")
            # print(f"line {line}")
            return True
    return False


def check_vertical(selected, board):
    flipped_board = flip_board(board)
    return check_horizontal(selected, flipped_board)

def flip_board(board):
    flipped_board = []
    for i in range(5):
        flipped_board.append([])
        for j in range(5):
            flipped_board[i].append(board[j][i])
    return flipped_board


def calculate_score(selected, board):
    single_list= board[0] + board[1] + board[2] + board[3] + board[4]
    single_list = [int(i) for i in single_list]
    for i in selected:
        try:
            single_list.remove(int(i))
        except ValueError:
            pass
    print(f"selected {selected}")
    print(f"board {board}")
    print(sum(single_list) * int( selected[-1] ))


with open("test") as f:
    file = f.read().splitlines()
    numbers = file[0].split(",")
    boards = find_boards(file[2:])
    for i in range(5, len(numbers)):
        winning = find_winning_board(numbers[:i], boards)
        selected = numbers[:i]
