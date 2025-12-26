from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [-10001] * m
        dp[0] = nums[0]

        for i in range(1, m):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
