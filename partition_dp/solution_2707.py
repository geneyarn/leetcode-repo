from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ws = set(dictionary)
        m = len(s)

        @cache
        def dp(idx: int) -> int:
            if idx == m:
                return 0
            ans = dp(idx + 1)
            for i in range(idx, m):
                sub = s[idx:i + 1]
                if sub in ws:
                    ans = max(ans, len(sub) + dp(i + 1))

            return ans

        match = dp(0)
        dp.cache_clear()
        return m - match


result = Solution().minExtraChar("leetscode", ["leet", "code", "leetcode"])
print(result)
