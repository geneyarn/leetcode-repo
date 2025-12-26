from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        i, j = 0, m - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1


# result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
result = Solution().search([3, 1], 1)
print(result)
