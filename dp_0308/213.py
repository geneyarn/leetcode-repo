from typing import List


class Solution:

    def robInner(self, nums: list[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]

        dp = [0] * m
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, m):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:

        m = len(nums)
        if m == 1:
            return nums[0]
        return max(self.robInner(nums[1:]), self.robInner(nums[:len(nums) - 1]))


# result = Solution().rob([2, 3, 2])
result = Solution().rob([1, 2, 3, 1])
print(result)
