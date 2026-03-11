from cmath import inf
from functools import cache


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0

            ans = inf
            mp = {}
            for j in range(i, m):
                mp[s[j]] = mp.get(s[j], 0) + 1

                valueSet = set(mp.values())
                if len(valueSet) == 1:
                    ans = min(ans, dp(j + 1) + 1)

            return ans

        res = dp(0)
        dp.cache_clear()
        return res


result = Solution().minimumSubstringsInPartition('fabccddg')
print(result)
