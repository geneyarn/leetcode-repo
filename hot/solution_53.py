from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-10000] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


result = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)
