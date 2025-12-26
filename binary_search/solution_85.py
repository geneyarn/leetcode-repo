from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left


# result = Solution().searchInsert([1, 3, 5, 6], 5)
result = Solution().searchInsert([1, 3, 5, 6], 4)
print(result)
