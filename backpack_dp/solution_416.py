from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        m = len(nums)
        if s % 2 != 0:
            return False

        target = s // 2

        @cache
        def dp(i: int, num: int) -> bool:
            if i < 0:
                return num == 0

            v = nums[i]
            if num >= v:
                return dp(i - 1, num) or dp(i - 1, num - v)
            else:
                return dp(i - 1, num)

        ans = dp(m - 1, target)
        dp.cache_clear()
        return ans


# result = Solution().canPartition([1, 5, 11, 5])
result = Solution().canPartition([2, 2, 3, 5])
print(result)
