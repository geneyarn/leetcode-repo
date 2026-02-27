from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all = sum(nums)
        m = len(nums)
        if all % 2 != 0:
            return False
        target = all // 2
        dp = [[False] * (target + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m + 1):
            n = nums[i - 1]
            for j in range(1, target + 1):
                if j >= n:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - n]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
