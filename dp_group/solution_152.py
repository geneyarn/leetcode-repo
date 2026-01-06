from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)
        big = [float('-inf')] * m
        small = [float('inf')] * m
        big[0] = nums[0]
        small[0] = nums[0]

        for i in range(1, m):
            big[i] = max(big[i - 1] * nums[i], nums[i], small[i - 1] * nums[i])
            small[i] = min(small[i - 1] * nums[i], nums[i], big[i - 1] * nums[i])

        return max(big)


result = Solution().maxProduct([2, 3, -2, 4])
print(result)
