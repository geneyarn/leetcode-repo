import math
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0
            if i == m - 1:
                return nums[-1]

            ans = dp(i + 1) + nums[i]
            ans = max(ans, dp(i + 2) + nums[i] - nums[i + 1])

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans

    def maximumTotalCost2(self, nums: List[int]) -> int:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0

            ans = -inf
            tmp = 0
            for j in range(i, m):
                tmp += int(nums[j] * math.pow(-1, j - i))
                ans = max(ans, dp(j + 1) + tmp)

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans


# result = Solution().maximumTotalCost([1, -2, 3, 4])
result = Solution().maximumTotalCost([1, -1, 1, -1])
print(result)
