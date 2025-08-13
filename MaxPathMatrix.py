def max_path_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create DP table
    dp = [[0] * cols for _ in range(rows)]
    print(dp)
    dp[0][0] = matrix[0][0]  # starting point
    print(dp)
    # Fill first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    print(dp)
    # Fill first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # Fill rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]


# Example
matrix = [
    [5, 3, 2, 1],
    [1, 2, 10, 2],
    [4, 3, 1, 5]
]

print(max_path_sum(matrix))  # Output: 29
