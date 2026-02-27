from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)

        @cache
        def dp(idx: int) -> bool:
            if idx >= len(s):
                return True
            ans = False
            for i in range(idx + 1, len(s) + 1):
                sub = s[idx: i]
                if sub in ws:
                    ans = ans or dp(i)
            return ans

        res = dp(0)
        dp.cache_clear()
        return res


result = Solution().wordBreak('leetcode', ["leet", "code"])
print(result)
