import json

class Sudokus:

    def __init__(self, filename):
        self.filename = filename


    def sudoku_checker(self):
        with open(self.filename) as file:    
            sudokus = json.load(file)

        for puzzle in sudokus:
            r = puzzle["box"][0]
            c = puzzle["box"][1]
            solution = puzzle["solution"]
            if self.check(solution, r, c):
                print puzzle["name"] + ": Correct"
            else:
                print puzzle["name"] + ": Incorrect"


    def check(self, solution, r, c):
        side_length = r * c
        n = list(range(1, side_length + 1))
        return (self.validate_rows(solution, r, c, n) and
            self.validate_columns(solution, r, c, n) and
            self.validate_grids(solution, r, c, n))


    def validate_rows(self, solution, r, c, n):
        for row in range(r):
            if sorted(solution[row]) != n:
                return False
        return True


    def validate_columns(self, solution, r, c, n):
        for col in range(r * c):
            column = []
            for row in range(r * c):
                column.append(solution[row][col])
            if sorted(column) != n:
                return False
        return True


    def validate_grids(self, solution, r, c, n):
        for row in range(0, r * c, r):
            for col in range(0, r * c, c):
                grid = []
                for sr in range(row, row + r):
                    for sc in range(col, col + c):
                        grid.append(solution[sr][sc])
                if sorted(grid) != n:
                    return False
        return True


if __name__ == "__main__":

    sudokus = Sudokus('sudokus.json')
    sudokus.sudoku_checker()