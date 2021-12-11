from pprint import pprint
import logging

logging.basicConfig(level=logging.INFO)


class DumboOctopusFlashed(Exception):
    """Dumbo Octopus flashed!"""

    def __str__(self):
        return "FLASH!"


class EverybodyFlashing(Exception):
    """All the octopuses are flashing"""

    def __str__(self):
        return "EVERYBODY FLASHIN'!"


class DumboOctopus:
    def __init__(self, energy, row, column):
        self.energy = energy
        self.row = row
        self.column = column
        self.flashed = False

    def __repr__(self):
        return f"{self.energy}"

    def increase_energy(self):
        if self.flashed is not True:
            self.energy += 1
            if (self.row, self.column) == (0, 0):
                logging.debug("Energy increased for (0,0).")

    def increase_energy_and_flash(self):
        self.increase_energy()
        self.check_flash()

    def check_flash(self):
        if self.energy > 9:
            self.flash()

    def flash(self):
        self.energy = 0
        self.flashed = True
        raise DumboOctopusFlashed

    def reset_flashed_state(self):
        self.flashed = False

    def print_coords(self):
        logging.debug("r %s c %s", self.row, self.column)


class OctopusBoard(object):
    def __init__(self, input):
        self.rows = len(input)
        self.columns = len(input[0])
        self.board = self._empty_board()
        self.flash_count = 0
        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column] = DumboOctopus(
                    energy=int(input[row][column]), row=row, column=column
                )

    def show_board(self):
        pprint(self.board)

    def _empty_board(self):
        board = []
        for row in range(self.rows):
            board.append([])
            for column in range(self.columns):
                board[row].append(None)
        return board

    def pulse(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column].increase_energy()

        for row in range(self.rows):
            for column in range(self.columns):
                try:
                    self.board[row][column].check_flash()
                except DumboOctopusFlashed as e:
                    logging.error(e)
                    self.flash_count += 1
                    self.notify_adjacent(row, column)

        if self.flash_count == self.rows * self.columns:
            raise EverybodyFlashing
        else:
            self.flash_count = 0

        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column].reset_flashed_state()

    def find_adjacent(self, row, column):
        rows = range(max(0, row - 1), min(self.rows - 1, row + 1) + 1)
        columns = range((max(0, column - 1)), min(self.columns - 1, column + 1) + 1)
        adjacent_octopuses = []
        for r in rows:
            for c in columns:
                if (r, c) != (row, column):
                    adjacent_octopuses.append(self.board[r][c])
                    self.board[r][c].print_coords()

        return adjacent_octopuses

    def notify_adjacent(self, row, column):
        logging.debug("Finding adjacent of %s %s", row, column)
        for octopus in self.find_adjacent(row, column):
            try:
                octopus.increase_energy_and_flash()
            except DumboOctopusFlashed:
                self.flash_count += 1
                self.notify_adjacent(octopus.row, octopus.column)


with open("test") as f:
    data = f.read().splitlines()
    octo_board = OctopusBoard(data)
    step = 0
    while True:
        step += 1
        try:
            octo_board.pulse()
        except EverybodyFlashing:
            logging.info(step)
            exit(1)
