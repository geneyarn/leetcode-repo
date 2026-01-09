from functools import cache
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]

            ans = nums[i] + dp(i - 1)
            ans = max(ans, nums[i - 1] - nums[i] + dp(i - 2))

            return ans

        ans = dp(m - 1)
        dp.cache_clear()
        return ans


result = Solution().maximumTotalCost([1, -2, 3, 4])
# result = Solution().maximumTotalCost([-5, 0, -5])
# result = Solution().maximumTotalCost([1, -1, 1, -1])
print(result)
