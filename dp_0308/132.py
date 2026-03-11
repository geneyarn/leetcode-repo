from cmath import inf
from functools import cache


class Solution:

    def minCut(self, s: str) -> int:
        m = len(s)

        @cache
        def valid(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0
            ans = inf
            for j in range(i, m):
                if valid(i, j):
                    ans = min(ans, dp(j + 1) + 1)
            return ans

        ans = dp(0)
        dp.cache_clear()
        valid.cache_clear()
        return ans - 1


result = Solution().minCut('aab')
print(result)
