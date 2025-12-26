from typing import List


class Solution:

    def __init__(self):
        self.wordSet = set()

    def dp(self, s: str, idx: int) -> List[str]:
        res = []

        if idx == len(s):
            res.append("")
            return res

        for i in range(idx + 1, len(s) + 1):
            prefix = s[idx:i]
            if prefix in self.wordSet:
                sub = self.dp(s, i)

                for s in sub:
                    if s == '':
                        res.append(prefix)
                    else:
                        res.append(prefix + " " + s)
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordSet = set(wordDict)

        return self.dp(s, 0)


result = Solution().wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
print(result)
