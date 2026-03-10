from cmath import inf
from functools import cache
from typing import List


class Solution:

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        s = set(targetIndices)

        @cache
        def dp(i: int, j: int) -> int:
            if i < j:
                return -inf
            # i >= j
            if i < 0 and j < 0:
                return 0

            ans = dp(i - 1, j) + (i in s)
            if j >= 0 and source[i] == pattern[j]:
                ans = max(dp(i - 1, j - 1), ans)

            return ans

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


# result = Solution().maxRemovals('abbaa', 'aba', [0, 1, 2])
# result = Solution().maxRemovals('bcda', 'd', [0, 3])
result = Solution().maxRemovals('yyey', 'y', [0])
# result = Solution().isSub('abbaa', 'aba')
print(result)
