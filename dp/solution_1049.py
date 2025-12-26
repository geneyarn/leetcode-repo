from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        m = sum(stones)
        n = len(stones)
        target = m // 2
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - stones[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])

        return m - dp[-1][-1] - dp[-1][-1]


result = Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1])
print(result)
