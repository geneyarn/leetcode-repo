import math


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        upper = math.ceil(math.pow(n, 1 / x))

        dp = [[0] * (n + 1) for _ in range(upper + 1)]
        dp[0][0] = 1

        for i in range(1, upper + 1):
            v = i ** x
            for j in range(n + 1):
                if j >= v:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - v]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] % (10 ** 9 + 7)


result = Solution().numberOfWays(10, 2)
# result = Solution().numberOfWays(4, 1)
# result = Solution().numberOfWays(2, 2)
print(result)
