class Solution:
    def numSquares(self, n: int) -> int:
        dp = [[n + 1] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            v = i ** 2

            for j in range(1, n + 1):
                if j >= v:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - v] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


result = Solution().numSquares(12)
print(result)
