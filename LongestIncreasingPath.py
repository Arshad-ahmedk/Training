from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        r, c = len(matrix), len(matrix[0])
        dp = [[0] * c for _ in range(r)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]

            maxadjpath = 1
            for dr, dc in directions:
                ar, ac = row + dr, col + dc
                if 0 <= ar < r and 0 <= ac < c and matrix[ar][ac] > matrix[row][col]:
                    maxadjpath = max(maxadjpath, 1 + dfs(ar, ac))

            dp[row][col] = maxadjpath
            return dp[row][col]

        maxlen = 0
        for row in range(r):
            for col in range(c):
                maxlen = max(maxlen, dfs(row, col))

        return maxlen


matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
]
print("Longest Increasing Path:", Solution().longestIncreasingPath(matrix))
