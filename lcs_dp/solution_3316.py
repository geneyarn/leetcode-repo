from functools import cache
from typing import List


class Solution:

    def isSub(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        @cache
        def dp(i: int, j: int) -> bool:
            if j < 0:
                return True
            if i < 0:
                return False

            if s[i] == t[j]:
                return dp(i - 1, j) or dp(i - 1, j - 1)
            else:
                return dp(i - 1, j)

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        fail = 0
        for i, idx in enumerate(targetIndices):

            s = source[:idx] + source[idx + 1:]
            sub = self.isSub(s, pattern)
            if not sub:
                fail += 1

        return len(targetIndices) - fail


# result = Solution().maxRemovals('abbaa', 'aba', [0, 1, 2])
# result = Solution().maxRemovals('bcda', 'd', [0, 3])
result = Solution().maxRemovals('dda', 'dda', [0, 1, 2])
print(result)
