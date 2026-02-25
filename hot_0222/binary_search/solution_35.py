from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        m = len(nums)
        i, j = 0, m - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1

        return i
