from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        m = len(nums)

        for i in range(m):
            if nums[i] > m or nums[i] <= 0:
                nums[i] = m + 1

        for i in range(m):
            v = abs(nums[i])
            if v > m:
                continue
            nums[v - 1] = -abs(nums[v - 1])

        for i in range(m):
            if nums[i] >= 0:
                return i + 1
        return m + 1


result = Solution().firstMissingPositive([1, 2, 0])
# result = Solution().firstMissingPositive([1])
print(result)
