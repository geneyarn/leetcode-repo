from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        m = len(nums)
        i, j = 0, 0

        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < m:
            nums[i] = 0
            i += 1


arr = [0, 1, 0, 3, 12]
resutl = Solution().moveZeroes(arr)
print(arr)
