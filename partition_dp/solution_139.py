from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        ws = set(wordDict)
        dp = [True] + [False] * m

        for i in range(1, m + 1):
            for j in range(i):
                sub = s[j:i]
                if dp[j] and sub in ws:
                    dp[i] = True
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        m = len(s)

        @cache
        def dp(i: int) -> bool:
            if i >= m:
                return True
            ans = False
            for j in range(i + 1, m + 1):
                sub = s[i:j]
                if sub in ws:
                    ans = dp(j)
                if ans:
                    return True

            return ans

        return dp(0)


result = Solution().wordBreak('leetcode', ['leet1', 'code'])
print(result)
