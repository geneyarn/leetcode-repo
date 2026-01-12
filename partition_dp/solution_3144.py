from functools import cache
from math import inf


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            ans = inf
            for j in range(i + 1):
                sub = s[j:i + 1]
                mp = {}
                for c in sub:
                    mp[c] = mp.get(c, 0) + 1
                vSet = set(mp.values())
                if len(vSet) == 1:
                    ans = min(1 + dp(j - 1), ans)
            return ans

        result = dp(m - 1)
        dp.cache_clear()
        return result


# result = Solution().minimumSubstringsInPartition('fabccddg')
result = Solution().minimumSubstringsInPartition('abababaccddb')
print(result)
