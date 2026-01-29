from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        ws = set(wordDict)

        dp = [False] * (m + 1)
        dp[0] = True

        for i in range(1, m + 1):
            for j in range(i):
                if s[j:i] in ws and dp[j]:
                    dp[i] = True

        return dp[-1]


# result = Solution().wordBreak('leetcode', ["leet", "code"])
result = Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
print(result)
