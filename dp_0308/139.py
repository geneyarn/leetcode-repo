from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        ws = set(wordDict)

        @cache
        def dp(i: int) -> bool:
            if i == m:
                return True

            ans = False
            for j in range(i + 1, m + 1):
                sub = s[i:j]
                if sub in ws:
                    ans = ans or dp(j)

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans


result = Solution().wordBreak('leetcode1', ["leet", "code"])
print(result)
