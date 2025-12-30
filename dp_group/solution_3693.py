from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(max(i - 3, 0), i):
                dp[i] = min(dp[j] + (i - j) * (i - j), dp[i])
            dp[i] += costs[i - 1]
            # dp[i] = min(dp[i - 1] + costs[i - 1] + math.pow(1, 2), dp[i])
            #
            # if i - 2 >= 0:
            #     dp[i] = min(dp[i - 2] + costs[i - 1] + math.pow(2, 2), dp[i])
            # if i - 3 >= 0:
            #     dp[i] = min(dp[i - 3] + costs[i - 1] + math.pow(3, 2), dp[i])

        return int(dp[-1])


result = Solution().climbStairs(4, [1, 2, 3, 4])
# result = Solution().climbStairs(4, [5, 1, 6, 2])
print(result)
