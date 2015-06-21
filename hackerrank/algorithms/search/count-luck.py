def map_forest(rows, columns):
    forest = []
    for i in range(rows):
        line = list(raw_input())
        if "M" in line:
            hermione = str(r) + " " + str(line.index("M"))
        elif "*" in line:
            exit = str(r) + " " + str(line.index("*"))
        forest.append(line)
    return forest, hermione, exit

def count_waves(forest, hermione, exit):
    h_row, h_column = hermione.split()
    e_row, e_column = exit.split()
    hermione = forest[h_row][h_column]
    exit = forest[e_row][e_column]
    for r in range(rows * columns):
        if forest[h_row + 1][h_column] == ".":
            up = True
        if forest[h_row - 1][h_column] == ".":
            down = True
        if forest[h_row][h_column + 1] == ".":
            right = True
        if forest[h_row][h_column - 1] == ".":
            left = True

test_cases = int(raw_input())

for case in range(test_cases):
    rows, columns = (int(x) for x in raw_input().split())
    forest, hermione, exit = map_forest(rows, columns)