from cmath import inf
from functools import cache

pow5 = [bin(5 ** i)[2:] for i in range(7)]


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
            for t in pow5:
                if i + len(t) > m:
                    break

                if s[i:i + len(t)] == t:
                    ans = min(ans, dp(i + len(t)) + 1)
            return ans

        res = dp(0)
        dp.cache_clear()
        return res


result = Solution().minimumBeautifulSubstrings('1011')
print(result)
