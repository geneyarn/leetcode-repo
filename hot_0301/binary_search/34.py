from typing import List


class Solution:

    def leftBound(self, nums: list[int], target: int) -> int:
        m = len(nums)
        i, j = 0, m - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        if i < 0 or i >= m or nums[i] != target:
            return -1

        return i

    def rightBound(self, nums: list[int], target: int) -> int:
        m = len(nums)
        i, j = 0, m - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1

        if j < 0 or j >= m or nums[j] != target:
            return -1

        return j

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftBound(nums, target), self.rightBound(nums, target)]
