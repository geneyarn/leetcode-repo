from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m = len(nums)
        mi = [float('inf')] * m
        ma = [float('-inf')] * m

        mi[0] = ma[0] = nums[0]

        for i in range(1, m):
            mi[i] = min(mi[i - 1] + nums[i], nums[i])
            ma[i] = max(ma[i - 1] + nums[i], nums[i])

        return max(abs(max(ma)), abs(min(mi)))


# result = Solution().maxAbsoluteSum([1, -3, 2, 3, -4])
result = Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2])
print(result)
