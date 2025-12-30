from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        m = len(s)
        ws = set(dictionary)

        def dp(idx: int) -> int:
            ans = 0
            for i in range(idx, m + 1):
                for j in range(0, i):
                    v = s[j:i]
                    if v in ws:
                        ans = max(ans, len(v) + dp(i))
            return ans

        return dp(0)


result = Solution().minExtraChar('leetscode', ["leet", "code", "leetcode"])
print(result)
