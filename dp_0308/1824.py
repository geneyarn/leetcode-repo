from cmath import inf
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        m = len(obstacles)
        dp = [[inf] * 3 for _ in range(m)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1

        for i in range(1, m):
            minV = inf
            for j in range(6):
                idx = j % 3
                if obstacles[i] == idx + 1:
                    dp[i][idx] = inf
                else:
                    dp[i][idx] = min(dp[i - 1][idx], minV + 1)
                minV = min(minV, dp[i][idx])

        ans = inf
        for i in range(3):
            ans = min(dp[-1][i], ans)

        return ans


result = Solution().minSideJumps([0, 1, 2, 3, 0])
print(result)
