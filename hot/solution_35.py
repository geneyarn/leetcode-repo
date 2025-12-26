from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            mid = (i + j) // 2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid + 1

        return i
