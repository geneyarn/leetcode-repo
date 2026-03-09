from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = len(nums)
        s = sum(nums)

        mx = [0] * (m)
        mi = [0] * (m)

        mx[0] = mi[0] = nums[0]

        for i in range(1, m):
            mx[i] = max(mx[i - 1] + nums[i], nums[i])
            mi[i] = min(mi[i - 1] + nums[i], nums[i])

        maxVal = max(mx)
        minVal = min(mi)

        if maxVal < 0:
            return maxVal

        return max(maxVal, s - minVal)


result = Solution().maxSubarraySumCircular([5, -3, 5])
print(result)
