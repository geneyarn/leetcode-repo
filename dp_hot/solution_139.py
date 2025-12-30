from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        ws = set(wordDict)

        @cache
        def dp(idx: int) -> bool:
            if idx >= m:
                return True
            ans = False
            for i in range(idx, m + 1):
                if s[idx:i] in ws:
                    ans = ans or dp(i)
            return ans

        return dp(0)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in ws:
                    dp[i] = True

        return dp[-1]


result = Solution().wordBreak('leetcode', ["leet", "code"])
print(result)
