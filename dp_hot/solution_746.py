from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m = len(cost)
        dp = [0] * (m + 1)

        if m <= 2:
            return dp[m - 1]

        for i in range(2, m + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]


# result = Solution().minCostClimbingStairs([10, 15, 20])
result = Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
# [0, 0, 1, 2, 2, 3, 3, 4, 4, 5]
# [0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 6]
print(result)
