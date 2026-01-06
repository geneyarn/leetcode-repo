import math
from cmath import inf
from functools import cache


class Solution:
    def numSquares(self, n: int) -> int:
        big = math.ceil(math.pow(n, 0.5))
        dp = [[inf] * (n + 1) for _ in range(big + 1)]
        dp[0][0] = 0

        for i in range(1, big + 1):
            v = i ** 2
            for j in range(n + 1):
                if j >= v:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - v] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def numSquares2(self, n: int) -> int:

        big = math.ceil(math.pow(n, 0.5))

        @cache
        def dp(i: int, num: int) -> int:

            if i == 0:
                return 0 if num == 0 else inf
            v = i ** 2
            if num >= v:
                return min(dp(i - 1, num), dp(i, num - v) + 1)
            else:
                return dp(i - 1, num)

        ans = dp(big, n)
        dp.cache_clear()
        return ans


result = Solution().numSquares(12)
print(result)
