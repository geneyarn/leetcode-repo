from functools import cache
from typing import List


class Solution:
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s + target) % 2 != 0:
            return False

        newTarget = (s + target) // 2
        m = len(nums)
        dp = [[0] * (newTarget + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, newTarget + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # s1 + s2 = sum
        # s1 - s2 = target
        s = sum(nums)
        if (s + target) % 2 != 0:
            return 0

        newTarget = (s + target) // 2
        m = len(nums)

        @cache
        def dp(i: int, t: int) -> int:
            if i < 0:
                return 0 if t != 0 else 1
            # if i >= m:
            #     return 0
            # if t == 0:
            #     return 1

            if nums[i] > t:
                return dp(i - 1, t)
            else:
                return dp(i - 1, t) + dp(i - 1, t - nums[i])

        return dp(m - 1, newTarget)


# result = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
result = Solution().findTargetSumWays([1], 2)
print(result)
