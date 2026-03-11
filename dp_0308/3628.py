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
                return dp(i - 1, j) + dp(i - 1, j - 1)
            return dp(i - 1, j)

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans

    def calcuteInsertC(self, s: str) -> int:
        t = s.count('T')
        l = 0
        ans = 0

        for c in s:
            if c == 'T':
                t -= 1
            elif c == 'L':
                l += 1

        ans = max(ans, t * l)
        return ans

    def numOfSubsequences(self, s: str) -> int:
        m = len(s)

        ext = max(self.numDistinct(s, 'LC'), self.numDistinct(s, 'CT'), self.calcuteInsertC(s))

        return self.numDistinct(s, 'LCT') + ext


result = Solution().numOfSubsequences('LMCT')
print(result)
