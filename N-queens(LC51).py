def solveNQueens(n):
    solutions = []

    rowf = [False for _ in range(n)]
    colf = [False for _ in range(n)]
    t1d = [False for _ in range(2*n+1)]
    t2d = [False for _ in range(2*n+1)]
    board = [["."]*n for _ in range(n)]

    def fill(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if rowf[row] or colf[col] or t1d[row + col] or t2d[row - col + n]:
                continue
            board[row][col] = "Q"
            rowf[row] = colf[col] = t1d[row + col] = t2d[row - col + n] = True

            fill(row + 1)

            board[row][col] = "."
            rowf[row] = colf[col] = t1d[row + col] = t2d[row - col + n] = False

    fill(0)
    return solutions

res = solveNQueens(4)
for solution in res:
    for row in solution:
        print(row)
    print()
