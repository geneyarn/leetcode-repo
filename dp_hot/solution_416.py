from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        m = len(nums)

        dp = [[False] * (target + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


result = Solution().canPartition([1, 5, 11, 5])
print(result)
