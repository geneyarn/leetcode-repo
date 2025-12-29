from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)

        left = [1] * m
        right = [1] * m

        for i in range(1, m):
            left[i] = nums[i - 1] * left[i - 1]
        for j in range(m - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        res = [0] * m
        res[0] = right[0]
        res[-1] = left[-1]

        for i in range(1, m - 1):
            res[i] = left[i] * right[i]

        return res

result = Solution().productExceptSelf([1,2,3,4])
print(result)