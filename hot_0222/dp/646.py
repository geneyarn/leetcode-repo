from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        m = len(pairs)
        dp = [1] * m

        mx = 1
        for i in range(m):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    mx = max(dp[i], mx)

        return mx
