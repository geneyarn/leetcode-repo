from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        if (s + target) % 2 != 0:
            return 0

        newTarget = (s + target) // 2
        m = len(nums)

        dp = [[0] * (newTarget + 1) for _ in range(m + 1)]

        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(newTarget + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


# result = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
result = Solution().findTargetSumWays([0], 0)
print(result)
