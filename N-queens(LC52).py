# def nqueen(n):
#     global ways
#     ways = False
#     rowf,colf = [False for _ in range(n)],[False for _ in range(n)]
#     t1d,t2d = [False for _ in range(2*n+1)],[False for _ in range(2*n+1)]
#     fill(n, 0, rowf, colf, t1d, t2d)
#     return ways
#
# def fill(n, row, rowf, colf, t1d, t2d):
#     global ways
#     if row == n:
#         ways += 1
#         return
#     for col in range(n):
#         if rowf[row] or colf[col] or t1d[row + col] or t2d[row - col + n] :
#             continue
#         rowf[row] = colf[col] = t1d[row + col] = t2d[row - col + n] = True
#         fill(n, row + 1, rowf, colf, t1d, t2d)
#         rowf[row] = colf[col] = t1d[row + col] = t2d[row - col + n] = False
#
# print(nqueen(4))
# print(nqueen(8))

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        cols = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                # Remove queen (backtrack)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return count

print(Solution().totalNQueens(4))