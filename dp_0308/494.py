from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = len(nums)
        s = sum(nums)
        if (s + target) % 2 != 0:
            return 0

        newTarget = (s + target) // 2

        @cache
        def dp(i: int, t: int) -> int:
            if i < 0:
                return 1 if t == 0 else 0

            if nums[i] <= t:
                return dp(i - 1, t - nums[i]) + dp(i - 1, t)

            return dp(i - 1, t)

        ans = dp(m - 1, newTarget)
        dp.cache_clear()
        return ans

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        m = len(nums)
        s = sum(nums)
        if (s + target) % 2 != 0:
            return 0

        newTarget = (s + target) // 2

        dp = [[0] * (newTarget + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            v = nums[i - 1]
            for j in range(1, newTarget + 1):
                if j >= v:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - v]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


result = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
print(result)
