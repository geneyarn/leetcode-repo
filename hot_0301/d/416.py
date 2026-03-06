from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = len(nums)
        all = sum(nums)
        if all % 2 != 0:
            return False

        target = all // 2
        dp = [[False] * (target + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m + 1):
            v = nums[i - 1]
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= v:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - v]

        return dp[-1][-1]


result = Solution().canPartition([1, 5, 11, 5])
print(result)
