class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        dp[1] = 1
        dp[2] = 2
        # dp[3] =
        pass
