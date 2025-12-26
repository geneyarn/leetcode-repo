from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [m] * m
        dp[0] = 0

        for i in range(m):
            step = nums[i]
            for j in range(1, step + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]
