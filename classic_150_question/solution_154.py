from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = len(nums)
        l, r = 0, m - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[r]:
                r -= 1
                continue
            else:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
        return nums[l]


result = Solution().findMin([2, 2, 2, 0, 1])
print(result)
