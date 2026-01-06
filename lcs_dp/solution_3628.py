from functools import cache


class Solution:

    def inner(self, s: str, t: str) -> int:
        m = len(s)

        @cache
        def dp(i: int, j: int) -> int:
            if j < 0:
                return 1
            if i < 0:
                return 0

            if s[i] == t[j]:
                return dp(i - 1, j) + dp(i - 1, j - 1)
            else:
                return dp(i - 1, j)

        ans = dp(m - 1, len(t) - 1)
        dp.cache_clear()
        return ans

    def calculateC(self, s: str) -> int:
        tCount = s.count('T')
        lCount = 0
        ans = 0
        for c in s:
            if c == 'T':
                tCount -= 1
            elif c == 'L':
                lCount += 1
            ans = max(ans, tCount * lCount)
        return ans

    def numOfSubsequences(self, s: str) -> int:
        ext = max(self.inner(s, 'LC'), self.inner(s, 'CT'), self.calculateC(s))

        return self.inner(s, 'LCT') + ext


# result = Solution().numOfSubsequences('LMCT')
result = Solution().numOfSubsequences('LCCT')
print(result)
