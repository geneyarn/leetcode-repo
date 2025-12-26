class Solution:
    def minInsertions(self, s: str) -> int:
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = 0

        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        return dp[0][-1]


# result = Solution().minInsertions('zzazz')
# result = Solution().minInsertions('leetcode')
result = Solution().minInsertions('zjveiiwvc')
print(result)
