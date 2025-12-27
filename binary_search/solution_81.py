from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        m = len(nums)
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            # todo: what if nums[mid] == num[r] nums[l] == nums[mid]

            if nums[l] == nums[mid]:
                l += 1
                continue
            if nums[r] == nums[mid]:
                 r -= 1
                 continue

            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


# result = Solution().search([2, 5, 6, 0, 0, 1, 2], 3)
# result = Solution().search([1], 3)
# result = Solution().search([1, 0, 1, 1, 1], 0)
result = Solution().search([4,5,6,7,0,1,2], 0)
print(result)
