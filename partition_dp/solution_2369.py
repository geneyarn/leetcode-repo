from functools import cache
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        m = len(nums)

        @cache
        def dp(i: int) -> bool:
            if i < 0:
                return True

            two = i - 1 >= 0 and nums[i] == nums[i - 1] and dp(i - 2)
            three = i - 2 >= 0 and nums[i] == nums[i - 1] == nums[i - 2] and dp(i - 3)
            threeCrease = i - 2 >= 0 and nums[i - 2] + 1 == nums[i - 1] and nums[i - 1] + 1 == nums[i] and dp(i - 3)

            return two or three or threeCrease

        ans = dp(m - 1)
        dp.cache_clear()
        return ans


# result = Solution().validPartition([4, 4, 4, 5, 6])
result = Solution().validPartition([1, 1, 1, 2])
print(result)
