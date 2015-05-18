import json

from sudokus import Sudokus

class Sudokus3D(Sudokus):

    def __init__(self, filename):
        Sudokus.__init__(self, filename)


    def sudoku3d_checker(self):
        with open(self.filename) as file:    
            sudokus = json.load(file)

        for puzzle in sudokus:
            r = puzzle["box"][0]
            c = puzzle["box"][1]
            solution = puzzle["solution"]
            if self.check3d(solution, r, c):
                print puzzle["name"] + ": Correct"
            else:
                print puzzle["name"] + ": Incorrect"


    def check3d(self, solution, r, c):
        for grid in solution:
            if not self.check(grid, r, c):
                return False
        if not self.validate_z(solution, r, c):
            return False
        return True


    def validate_z(self, solution, r, c):
        for col in range(r * c):
            side = []
            overhead = []
            for row in range(r * c):
                depth = []
                for z in range(r * c):
                    depth.append(solution[z][row][col])
                side.append(depth)
                overhead.append(solution[row][col])
            if not (self.check(side, r, c) and
                self.check(overhead, r, c)):
                return False
        return True


if __name__ == "__main__":

    sudokus3d = Sudokus3D('sudokus3d.json')
    sudokus3d.sudoku3d_checker()