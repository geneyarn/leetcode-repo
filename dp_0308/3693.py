from cmath import inf
from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 0

            ans = inf
            for j in range(max(i - 3, 0), i):
                ans = min(ans, dp(j) + (i - j) ** 2)

            ans += costs[i - 1]

            return ans

        return dp(n)

    def climbStairs2(self, n: int, costs: List[int]) -> int:
        m = len(costs)
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = costs[i - 1] + min(
                dp[i - 1] + 1,
                dp[i - 2] + 2 ** 2 if i - 2 >= 0 else inf,
                dp[i - 3] + 3 ** 2 if i - 3 >= 0 else inf
            )
        return dp[-1]


result = Solution().climbStairs(4, [1, 2, 3, 4])
print(result)
