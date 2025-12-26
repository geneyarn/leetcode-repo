from typing import List


class Solution:

    def robInner(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        m = len(nums)
        dp = [0] * m

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, m):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.robInner(nums[:len(nums) - 1]), self.robInner(nums[1:]))


result = Solution().rob([0])
print(result)
