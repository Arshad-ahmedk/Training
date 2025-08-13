def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end_index_s1 = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index_s1 = i
            else:
                dp[i][j] = 0

    return s1[end_index_s1 - max_len: end_index_s1]

print(longest_common_substring("pot", "jackpot"))
