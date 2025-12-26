from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        pre = [0] * m
        pre[0] = nums[0]
        for i in range(1, m):
            pre[i] = pre[i - 1] * nums[i]

        suffix = [0] * m
        suffix[-1] = nums[-1]
        for i in range(m - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        res = [0] * len(nums)
        res[0] = suffix[1]
        res[-1] = pre[m - 2]

        for i in range(1, m - 1):
            res[i] = pre[i - 1] * suffix[i + 1]

        return res


result = Solution().productExceptSelf([1, 2, 3, 4])
print(result)
