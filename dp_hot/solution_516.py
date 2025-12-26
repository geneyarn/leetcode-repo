class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        dp = [[0] * m for _ in range(m)]

        for i in range(m):
            dp[i][i] = 1
        result = 0

        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return result
