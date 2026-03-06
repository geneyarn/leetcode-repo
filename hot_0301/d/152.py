from cmath import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)

        mx = [-inf] * m
        mi = [inf] * m

        mx[0] = mi[0] = nums[0]

        for i in range(1, m):
            mx[i] = max(mx[i - 1] * nums[i], nums[i], mi[i - 1] * nums[i])
            mi[i] = min(mx[i - 1] * nums[i], nums[i], mi[i - 1] * nums[i])

        return max(mx)


result = Solution().maxProduct([2, 3, -2, 4])
print(
    result
)
