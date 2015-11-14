def valid_in_row(row, n):
    return n not in row

def valid_in_col(board, c, n):
    for row in board:
        if row[c] == n:
            return False
    return True

def valid_in_subgrid(board, r, c, n):
    subgrids = [(0, 3), (3, 6), (6, 9)]
    for subgrid in subgrids:
        if r >= subgrid[0] and r < subgrid[1]:
            rows = subgrid
        if c >= subgrid[0] and c < subgrid[1]:
            cols = subgrid
    for row in range(rows[0], rows[1]):
        for col in range(cols[0], cols[1]):
            if board[row][col] == n:
                return False
    return True

def sudoku_solver(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                for n in range(1, 10):
                    if (valid_in_row(board[r], n) and
                        valid_in_col(board, c, n) and
                        valid_in_subgrid(board, r, c, n)):
                        board[r][c] = n
                        valid_board = sudoku_solver(board)
                        if valid_board:
                            return valid_board
                return None

board = [[0, 4, 8, 2, 0, 0, 9, 3, 5],
         [0, 0, 0, 3, 7, 1, 0, 6, 8],
         [9, 0, 0, 6, 0, 0, 0, 0, 1],
         [7, 2, 1, 0, 0, 4, 8, 0, 0],
         [0, 8, 0, 0, 5, 3, 0, 2, 0],
         [0, 0, 4, 1, 0, 0, 3, 0, 7],
         [3, 6, 0, 0, 9, 0, 1, 0, 0],
         [4, 0, 2, 8, 2, 0, 5, 0, 0],
         [0, 9, 0, 0, 0, 7, 0, 8, 4]]

print sudoku_solver(board)
