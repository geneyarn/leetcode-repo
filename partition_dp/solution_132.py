from functools import cache
from math import inf


class Solution:
    def minCut(self, s: str) -> int:
        m = len(s)

        @cache
        def is_pan(l: int, r: int) -> bool:
            if l >= r:
                return True
            return s[l] == s[r] and is_pan(l + 1, r - 1)

        @cache
        def dp(r: int) -> int:
            if is_pan(0, r):
                return 0
            ans = inf
            for i in range(1, r + 1):
                if is_pan(i, r):
                    ans = min(ans, dp(i - 1) + 1)
            return ans

        return dp(m - 1)


# result = Solution().minCut('aab')
# result = Solution().minCut('a')
# result = Solution().minCut('ab')
# result = Solution().minCut('ababbbabbaba')
result = Solution().minCut('leet')
print(result)
