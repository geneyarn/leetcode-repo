from typing import List


class Solution:

    def __init__(self):
        self.wordSet = set()
        self.memo = []

    def dp(self, s: str, idx: int):
        if idx == len(s):
            return True

        if self.memo[idx] != -1:
            return True if self.memo[idx] == 1 else False

        for i in range(idx + 1, len(s) + 1):
            prefix = s[idx: i]
            if prefix in self.wordSet:
                if self.dp(s, i):
                    self.memo[idx] = 1
                    return True
        self.memo[idx] = 0
        return False

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        self.memo = [-1] * len(s)

        return self.dp(s, 0)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)

        self.wordSet = set(wordDict)

        dp = [False] * (m + 1)
        dp[0] = True

        for i in range(1, m + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in self.wordSet:
                    dp[i] = True

        return dp[-1]


# result = Solution().wordBreak('leetcode', ["leet", "code"])
result = Solution().wordBreak('applepenapple', ["apple", "pen"])
# result = Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
print(result)
