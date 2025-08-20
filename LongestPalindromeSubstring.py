# Using DP
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]

    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length

    return s[start:start + max_len]


print(longestPalindrome("babad"))
print(longestPalindrome("ccc"))


# # Expanding Around Center
# def longestPalindrome(s: str) -> str:
#     if not s:
#         return ""
#
#     start, end = 0, 0
#
#     def expandAroundCenter(left: int, right: int) -> (int, int):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1
#
#     for i in range(len(s)):
#
#         l1, r1 = expandAroundCenter(i, i)
#
#         l2, r2 = expandAroundCenter(i, i + 1)
#
#
#         if r1 - l1 > end - start:
#             start, end = l1, r1
#         if r2 - l2 > end - start:
#             start, end = l2, r2
#
#     return s[start:end + 1]
#
# if __name__ == "__main__":
#     print(longestPalindrome("babad"))
#     print(longestPalindrome("cbbd"))
#     print(longestPalindrome("a"))
#     print(longestPalindrome("ac"))
