from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ws = set(dictionary)
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0

            ans = 0
            for j in range(i + 1, m + 1):
                sub = s[i:j]
                if sub in ws:
                    ans = max(ans, dp(j) + len(sub))

            ans = max(ans, dp(i + 1))

            return ans

        t = dp(0)
        dp.cache_clear()
        return len(s) - t


result = Solution().minExtraChar('leetscode', ["leet", "code", "leetcode"])
print(result)
