from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)

        dp = [m + 1] * m
        dp[0] = 0

        for i in range(m):
            for j in range(1, nums[i] + 1):
                if i + j < m:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]
