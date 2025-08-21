# import math
# from typing import List
#
# class Solution:
#     def solveSudoku(self, board: List[List[str]],n:int) -> None:
#         m=int(math.sqrt(n))
#         rows = [set() for _ in range(n)]
#         cols = [set() for _ in range(n)]
#         boxes = [set() for _ in range(n)]
#         empties = []
#
#         for r in range(n):
#             for c in range(n):
#                 if board[r][c] == '.':
#                     empties.append((r, c))
#                 else:
#                     val = board[r][c]
#                     rows[r].add(val)
#                     cols[c].add(val)
#                     boxes[(r//m)*m + (c//m)].add(val)
#
#         def backtrack(idx=0):
#             if idx == len(empties):
#                 return True
#             r, c = empties[idx]
#             b = (r//m)*m + (c//m)
#             for num in range(1,n+1):
#                 if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
#                     board[r][c] = num
#                     rows[r].add(num)
#                     cols[c].add(num)
#                     boxes[b].add(num)
#
#                     if backtrack(idx + 1):
#                         return True
#
#                     board[r][c] = '.'
#                     rows[r].remove(num)
#                     cols[c].remove(num)
#                     boxes[b].remove(num)
#             return False
#
#         backtrack()
#



import math
def getfree(board,n):
    for row in range(n):
        for col in range(n):
            if board[row][col] == ".":
                return (row, col)
    return None


def isValid(board, row, col, c):
    n = len(board)
    m = int(math.sqrt(n))
    c = str(c)
    for k in range(n):
        if board[row][k] == c or board[k][col] == c:
            return False
    boxRow, boxCol = m * (row // m), m * (col // m)
    for i in range(boxRow, boxRow + m):
        for j in range(boxCol, boxCol + m):
            if board[i][j] == c:
                return False
    return True


def fill(board,n):
    cell = getfree(board,n)
    if not cell:
        return True

    row, col = cell
    for num in range(1, n+1):
        if isValid(board, row, col, num):
            board[row][col] = str(num)
            if fill(board,n):
                return True
            board[row][col] = "."

    return False

# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

board =[
["5",".",".",".",".",".",".",".","7",".",".",".",".",".",".","."],
[".",".",".","2",".",".",".",".",".","9",".",".",".",".",".","."],
[".",".","8",".",".","7",".",".",".",".",".","6",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","3"],
[".",".",".",".","3",".",".",".",".",".",".",".",".","12",".","."],
[".","11",".",".",".",".","5",".",".",".",".",".",".",".","13","."],
[".",".",".",".",".",".",".","8",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
]

n=len(board)
fill(board,n)

for row in board:
    print(row)
