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
        else:
            from_top = dp[i-1][j] if i>0 else 0
            from_left = dp[i][j-1] if j>0 else 0
            if i != 0 or j != 0:
                dp[i][j] = from_top + from_left

print("DP Table:")
for row in dp:
    print(row)

print("Number of paths:", dp[-1][-1])
