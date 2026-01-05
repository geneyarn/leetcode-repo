import math
from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        big = math.ceil(math.pow(n, 1 / x))
        dp = [[0] * (n + 1) for _ in range(big + 1)]

        dp[0][0] = 1
        for i in range(1, big + 1):
            v = i ** x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= v:
                    dp[i][j] += dp[i - 1][j - v]

        return dp[-1][-1] % (10 ** 9 + 7)

    def numberOfWays2(self, n: int, x: int) -> int:
        big = math.ceil(math.pow(n, 1 / x))

        @cache
        def dp(i: int, num: int) -> int:

            if i == 0:
                return 1 if num == 0 else 0

            v = i ** x
            ans = dp(i - 1, num)
            if num >= v:
                ans += dp(i - 1, num - v)

            return ans

        ans = dp(big, n)
        dp.cache_clear()
        return ans % (10 * 9 + 7)


# result = Solution().numberOfWays(10, 2)
result = Solution().numberOfWays2(4, 1)
print(result)
