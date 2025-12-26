from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        m = len(nums)
        for i in range(m):
            if nums[i] > m or nums[i] <= 0:
                nums[i] = m + 1

        for i in range(m):
            n = abs(nums[i])
            if n > m:
                continue
            nums[n - 1] = -abs(nums[n - 1])

        for i in range(m):
            if nums[i] >= 0:
                return i + 1

        return m + 1


# result = Solution().firstMissingPositive([0, 1, 2])
# result = Solution().firstMissingPositive([3, 4, -1, 1])
# result = Solution().firstMissingPositive([7, 8, 9, 11, 12])
result = Solution().firstMissingPositive([1])
print(result)
