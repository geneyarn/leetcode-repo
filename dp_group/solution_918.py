from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = len(nums)
        ma = [0] * m
        mi = [0] * m
        ma[0] = nums[0]
        mi[0] = nums[0]

        for i in range(1, m):
            ma[i] = max(ma[i - 1] + nums[i], nums[i])
            mi[i] = min(mi[i - 1] + nums[i], nums[i])

        maxValue = max(ma)
        minValue = min(mi)
        if maxValue < 0:
            return maxValue
        return max(maxValue, sum(nums) - minValue)


# result = Solution().maxSubarraySumCircular([1, -2, 3, -2])
# result = Solution().maxSubarraySumCircular([5, -3, 5])
# result = Solution().maxSubarraySumCircular([-3, -2, -3])
result = Solution().maxSubarraySumCircular([8, -15, -29, -19])
print(result)
