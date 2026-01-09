from functools import cache
from math import inf


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0

            if s[i] == '0':
                return inf

            ans = inf
            l = 0
            for k in range(i, m):
                sub = s[i:k + 1]
                v = int(sub, 2)
                if v > 5 ** l:
                    l += 1
                if v == 5 ** l:
                    ans = min(ans, 1 + dp(k + 1))

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans if ans < inf else -1


# result = Solution().minimumBeautifulSubstrings('1011')
# result = Solution().minimumBeautifulSubstrings('111')
result = Solution().minimumBeautifulSubstrings('0')
print(result)
