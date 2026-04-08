from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        m = len(s)

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

        return dp(0)


result = Solution().wordBreak('leet1code', ["leet", "code"])
print(result)
