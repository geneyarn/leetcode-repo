from typing import List


class Solution:

    def searchLeft(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            mid = (i + j) // 2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid + 1
        if i >= len(nums):
            return -1
        return i if nums[i] == target else -1

    def searchRight(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid

        if i - 1 < 0 or i - 1 >= len(nums):
            return -1

        return i - 1 if nums[i - 1] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums, target), self.searchRight(nums, target)]
