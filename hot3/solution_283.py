from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)

        i, j = 0, 0
        while j < m:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1


arr = [0, 1, 0, 3, 12]
Solution().moveZeroes(arr)
print(arr)
