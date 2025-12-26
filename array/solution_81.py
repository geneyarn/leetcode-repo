from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        m = len(nums)
        i, j = 0, m - 1

        while i <= j:
            while i < j and nums[i] == nums[i + 1]:
                i += 1

            while i < j and nums[j] == nums[j - 1]:
                j -= 1

            mid = (i + j) // 2
            if nums[mid] == target:
                return True

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

        return False


# result = Solution().search([1], 1)
result = Solution().search([1], 2)
print(result)
