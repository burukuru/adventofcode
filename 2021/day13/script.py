import logging
from pprint import pprint

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

XAXIS = 0
YAXIS = 1


class OrigamiPaper:
    def __init__(self, dots, folds):
        self.dots = set(dots)
        self.folds = folds
        self.rows = self.max_coord(self.dots, YAXIS) + 1
        self.columns = self.max_coord(self.dots, XAXIS) + 1
        self.paper = self._fill_paper(self.dots)

        logger.debug("rows %s columns %s", self.rows, self.columns)

    def max_coord(self, dots, coord):
        max_coord = 0
        for dot in dots:
            max_coord = max(max_coord, dot[coord])

        return max_coord

    def _fill_paper(self, dots):
        paper = []
        logger.debug("Filling paper with dots")
        logger.debug("dots %s", dots)
        for row in range(self.rows):
            paper.append([])
            for column in range(self.columns):
                if (column, row) in dots:
                    paper[row].append("#")
                else:
                    paper[row].append(".")
        return paper

    def show_paper(self):
        for line in self.paper:
            print("".join(line))

    def fold_all(self):
        for fold in self.folds:
            axis, line_coord = fold.split("=")
            line_coord = int(line_coord)
            new_dots = self.fold(axis, line_coord)
            self.dots = new_dots
            self.count_dots()
            if axis == "x":
                self.columns = self.columns // 2
            elif axis == "y":
                logger.debug("folding vertically")
                self.rows = self.rows // 2
            self.paper = self._fill_paper(self.dots)

    def fold(self, axis, line_coord):
        new_dots = set()
        for dot in self.dots:
            if axis == "x" and dot[0] > line_coord:
                new_dot = (self.columns - dot[0] - 1, dot[1])
            elif axis == "y" and dot[1] > line_coord:
                new_dot = (dot[0], self.rows - dot[1] - 1)
            else:
                new_dot = dot
            logger.debug("Adding new dot %s", new_dot)
            new_dots.add(new_dot)
        return new_dots

    def count_dots(self):
        logger.debug(self.dots)
        print(len(self.dots))


with open("input") as file:
    data = file.read().split("\n\n")
    dots = data[0].splitlines()
    dots = [tuple(map(int, dot.split(","))) for dot in dots]

    folds = data[1].splitlines()
    folds = [fold.split()[-1] for fold in folds]

    ori_paper = OrigamiPaper(dots=dots, folds=folds)
    ori_paper.fold_all()
    ori_paper.show_paper()
