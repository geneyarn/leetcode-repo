from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @cache
        def dp(i: int, j: int, count: int) -> int:
            if i >= m or j >= n:
                return -inf
            if i == m - 1 and j == n - 1:
                return max(coins[i][j], 0) if count else coins[i][j]

            notDo = max(dp(i + 1, j, count), dp(i, j + 1, count)) + coins[i][j]
            doIt = -inf
            if coins[i][j] < 0 and count > 0:
                doIt = max(dp(i + 1, j, count - 1), dp(i, j + 1, count - 1))

            return max(doIt, notDo)

        return dp(0, 0, 2)


#
# result = Solution().maximumAmount([[0, 1, -1],
#                                    [1, -2, 3],
#                                    [2, -3, 4]])
# result = Solution().maximumAmount([[10, 10, 10], [10, 10, 10]])
result = Solution().maximumAmount([[-7, 12, 12, 13],
                                   [-6, 19, 19, -6],
                                   [9, -2, -10, 16],
                                   [-4, 14, -10, -9]])
print(result)
