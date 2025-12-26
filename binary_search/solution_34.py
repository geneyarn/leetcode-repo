from typing import List


class Solution:

    def leftBound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        if l < len(nums) and nums[l] == target:
            return l

        return -1

    def rightBound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        if r >= 0 and nums[r] == target:
            return r
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.leftBound(nums, target), self.rightBound(nums, target)]


# result = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
# result = Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
result = Solution().searchRange([2, 2], 3)
print(result)