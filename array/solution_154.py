from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = len(nums)
        i, j = 0, m - 1

        while i < j:
            mid = (i + j) // 2
            if nums[mid] == nums[j]:
                j -= 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1

        return nums[j]
