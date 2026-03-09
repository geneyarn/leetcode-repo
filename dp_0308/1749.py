from cmath import inf
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m = len(nums)
        mi = [inf] * m
        mi[0] = nums[0]
        mx = [-inf] * m
        mx[0] = nums[0]

        for i in range(1, m):
            mi[i] = min(mi[i - 1] + nums[i], nums[i])
            mx[i] = max(mx[i - 1] + nums[i], nums[i])

        return max(max(mx), abs(min(mi)))


result = Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2])
print(result)
