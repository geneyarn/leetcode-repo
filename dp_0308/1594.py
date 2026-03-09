from cmath import inf
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        mx = [[-inf] * n for _ in range(m)]
        mi = [[inf] * n for _ in range(m)]

        mx[0][0] = mi[0][0] = grid[0][0]

        for i in range(1, m):
            mx[i][0] = mx[i - 1][0] * grid[i][0]
            mi[i][0] = mi[i - 1][0] * grid[i][0]
        for j in range(1, n):
            mx[0][j] = mx[0][j - 1] * grid[0][j]
            mi[0][j] = mi[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                mx[i][j] = max(mx[i - 1][j] * grid[i][j], mx[i][j - 1] * grid[i][j], mi[i - 1][j] * grid[i][j],
                               mi[i][j - 1] * grid[i][j])
                mi[i][j] = min(mx[i - 1][j] * grid[i][j], mx[i][j - 1] * grid[i][j], mi[i - 1][j] * grid[i][j],
                               mi[i][j - 1] * grid[i][j])

        return mx[-1][-1] if mx[-1][-1] > 0 else -1


# result = Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]])
result = Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]])
print(result)
