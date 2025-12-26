from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# result = Solution().findPeakElement([1, 2, 3, 1])
# result = Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
result = Solution().findPeakElement([2, 1])
print(result)
