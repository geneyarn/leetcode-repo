from cmath import inf
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mp = {}

        for i in range(len(chars)):
            mp[chars[i]] = vals[i]

        m = len(s)
        dp = [-inf] * (m + 1)
        dp[0] = 0

        for i in range(1, m + 1):
            c = s[i - 1]
            val = mp.get(c, ord(c) - ord('a') + 1)
            dp[i] = max(dp[i - 1] + val, val)
        return max(dp)


# result = Solution().maximumCostSubstring('adaa', 'd', [-1000])
result = Solution().maximumCostSubstring('abc', 'abc', [-1, -1, -1])
print(result)
