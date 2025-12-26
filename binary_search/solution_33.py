from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
# result = Solution().search([1, 3], 3)
result = Solution().search([3, 1], -1)
print(result)
