from functools import cache
from math import inf
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
            ans = min(ans, dp[-1][i])

        return ans

    def minSideJumps2(self, obstacles: List[int]) -> int:
        m = len(obstacles)

        @cache
        def dp(i: int, j: int) -> int:
            if i >= m or j < 0 or j >= 3:
                return inf
            if obstacles[i] == j + 1:
                return inf
            if i == m - 1:
                return 0
            v = obstacles[i + 1]
            result = inf
            if v != j + 1:
                result = dp(i + 1, j)
            else:
                for k in range(3):
                    if k == j:
                        continue
                    result = min(result, dp(i, k) + 1)

            print(f'{i}-----{j}------{result}')
            return result

        return dp(0, 1)


# result = Solution().minSideJumps([0, 1, 2, 3, 0])
# result = Solution().minSideJumps([0, 1, 1, 3, 3, 0])
# result = Solution().minSideJumps([0, 2, 1, 0, 3, 0])
result = Solution().minSideJumps([0, 3, 3, 0, 3, 2, 2, 0, 0, 3, 0])
# result = Solution().minSideJumps([0, 3, 3, 0, 3, 2, 2, 0, 0, 3, 0])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
#  0  1  2  3  4  5  6  7  8  9  10

print(result)
