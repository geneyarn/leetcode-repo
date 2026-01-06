from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        m = len(s)
        dp = [0] * (m + 1)
        mp = {}
        for i in range(len(vals)):
            mp[chars[i]] = vals[i]

        for i in range(1, m + 1):
            c = s[i - 1]
            v = mp[c] if c in mp else (ord(c) - ord('a') + 1)
            dp[i] = max(dp[i - 1] + v, v, 0)

        return max(dp)


# result = Solution().maximumCostSubstring('adaa', 'd', [-1000])
result = Solution().maximumCostSubstring('abc', 'abc', [-1, -1, -1])
print(result)
