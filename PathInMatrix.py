a = [[0,0,0,0,1,1],
     [0,0,1,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,1,0,1],
     [0,0,0,0,0,0],
     [0,1,0,0,0,0]]

n, m = len(a), len(a[0])
dp = [[0]*m for _ in range(n)]

dp[0][0] = 1 if a[0][0] == 0 else 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dp[i][j] = 0
            continue
        if i == 0 and j == 0:
            continue
        top = dp[i-1][j] if i > 0 else 0
        left = dp[i][j-1] if j > 0 else 0
        dp[i][j] = top + left

print("DP Table:")
for row in dp:
    print(row)

print("Number of paths:", dp[-1][-1])
