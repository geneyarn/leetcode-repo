from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dp(i: int, j: int) -> int:
            if j < 0:
                return 1
            if i < 0:
                return 0
            if s[i] == t[j]:
                return dp(i - 1, j - 1) + dp(i - 1, j)
            else:
                return dp(i - 1, j)

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


# result = Solution().numDistinct('rabbbit', 'rabbit')
result = Solution().numDistinct('babgbag', 'bag')
print(result)
