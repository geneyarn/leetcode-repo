from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ws = set(dictionary)
        m = len(s)
        dp = [0] * (m + 1)

        for i in range(1, m + 1):
            for j in range(i):
                w = s[j:i]
                if w in ws:
                    dp[i] = max(dp[i], dp[j] + len(w))
                else:
                    dp[i] = max(dp[j], dp[i])

        return len(s) - dp[-1]

    def minExtraChar2(self, s: str, dictionary: List[str]) -> int:
        m = len(s)
        ws = set(dictionary)

        @cache
        def dp(idx: int) -> int:
            if idx == m:
                return 0
            ans = 0
            for i in range(idx, m):
                for j in range(i + 1, m + 1):
                    w = s[i:j]
                    if w in ws:
                        ans = max(ans, len(w) + dp(j))

            return ans

        return len(s) - dp(0)


result = Solution().minExtraChar('leetscode', ["leet", "code", "leetcode"])
# result = Solution().minExtraChar('sayhelloworld', ["hello", "world"])
print(result)
