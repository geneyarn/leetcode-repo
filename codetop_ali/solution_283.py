from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

            j += 1
        for k in range(i, len(nums)):
            nums[k] = 0
