from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l


# result = Solution().searchInsert([1, 3, 5, 6], 2)
result = Solution().searchInsert([1, 3, 5, 6], 5)
print(result)
