from typing import List


class Solution:
    # N = 3, W = 4
    # wt = [2, 1, 3]
    # val = [4, 2, 3]
    def knapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        dp = [[0] * (W + 1) for _ in range(len(wt))]

        for i in range(len(wt)):
            for j in range(1, W + 1):
                if j - wt[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i]] + val[i])

        return dp[-1][-1]


result = Solution().knapsack(1, [2, 1, 3], [4, 2, 3])
print(result)
