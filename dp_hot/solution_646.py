from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        m = len(pairs)
        dp = [1] * m

        for i in range(1, m):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return dp[-1]


result = Solution().findLongestChain([[1, 2], [2, 3], [3, 4]])
print(result)
