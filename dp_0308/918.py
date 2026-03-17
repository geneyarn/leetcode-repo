from cmath import inf
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = len(nums)
        s = sum(nums)

        mx = [-inf] * m
        mi = [inf] * m

        mx[0] = mi[0] = nums[0]

        for i in range(1, m):
            mx[i] = max(mx[i - 1] + nums[i], nums[i])
            mi[i] = min(mi[i - 1] + nums[i], nums[i])

        maxV = max(mx)
        minV = min(mi)

        if maxV < 0:
            return maxV

        return max(maxV, s - minV)


result = Solution().maxSubarraySumCircular([5, -3, 5])
print(result)
