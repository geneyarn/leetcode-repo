from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        m = len(s)

        @cache
        def dp(idx: int) -> bool:
            if idx == m:
                return True

            ans = False
            for i in range(idx + 1, m + 1):
                sub = s[idx: i]
                if sub in ws:
                    ans = ans or dp(i)

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans


result = Solution().wordBreak('leetcode1', ["leet", "code"])
print(result)
