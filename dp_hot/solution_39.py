from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = set(wordDict)
        m = len(s)
        dp = [False] * (m + 1)
        dp[0] = True

        for i in range(1, m + 1):
            for j in range(i):
                if dp[j] and s[j:i] in s:
                    dp[i] = True

        return dp[-1]
