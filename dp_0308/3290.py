from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0:
                return 0
            # i > =0
            if j < 0:
                return -inf

            return max(dp(i, j - 1), dp(i - 1, j - 1) + a[i] * b[j])

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


result = Solution().maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7])
print(result)
