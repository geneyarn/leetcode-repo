from math import inf
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[-1][-1] == -1 or grid[0][0] == -1:
            return 0

        def dp(i: int, j: int) -> int:
            if i >= n or j >= n:
                return -inf

            if i == n - 1 and j == n - 1:
                return 1 if grid[i][j] == 1 else 0

            if grid[i][j] == -1:
                return -inf

            count = 1 if grid[i][j] == 1 else 0
            grid[i][j] = 0
            return max(dp(i + 1, j), dp(i, j + 1)) + count

        return dp(0, 0)


arr = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
result = Solution().cherryPickup(arr)
print(result)
