from functools import cache
from math import inf
from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        s = set(targetIndices)

        @cache
        def dp(i: int, j: int) -> int:

            if i < j:
                return -inf
            if i < 0:
                return 0

            ans = dp(i - 1, j) + (i in s)
            if j >= 0 and source[i] == pattern[j]:
                ans = max(ans, dp(i - 1, j - 1))
            return ans

        ans = dp(len(source) - 1, len(pattern) - 1)
        dp.cache_clear()
        return ans


result = Solution().maxRemovals('abbaa', 'aba', [0, 1, 2])
print(result)
