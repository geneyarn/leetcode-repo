from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)

        dp = [1] * m

        mx = 1
        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

                mx = max(mx, dp[i])
        return mx
