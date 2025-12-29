from functools import cache
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        m = len(words)
        ws = set(words)
        @cache
        def dp(s: str) -> int:
            ans = 0

            for i in range(len(s)):
                t = s[:i] + s[i+1:]
                if t in ws:
                    ans = max(ans, dp(t))
            return ans + 1

        return max([dp(s) for s in words])

result = Solution().longestStrChain(["a","b","ba","bca","bda","bdca"])
print(result)
