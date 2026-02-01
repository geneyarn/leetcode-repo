from typing import List


class Solution:

    def leftBound(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l if l < m and nums[l] == target else -1

    def rightBound(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r if r >= 0 and nums[r] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftBound(nums, target), self.rightBound(nums, target)]


result = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
print(result)
