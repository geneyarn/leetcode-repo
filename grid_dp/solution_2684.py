from functools import cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, v: int) -> int:
            if j + 1 >= n:
                return 0
            v1 = v2 = v3 = 0
            if grid[i][j + 1] > v:
                v1 = 1 + dfs(i, j + 1, grid[i][j + 1])
            if i - 1 >= 0 and grid[i - 1][j + 1] > v:
                v2 = 1 + dfs(i - 1, j + 1, grid[i - 1][j + 1])
            if i + 1 < m and grid[i + 1][j + 1] > v:
                v3 = 1 + dfs(i + 1, j + 1, grid[i + 1][j + 1])

            return max(v1, v2, v3)

        result = 0
        for k in range(m):
            tmp = dfs(k, 0, grid[k][0])
            result = max(result, tmp)
        return result


# result = Solution().maxMoves([[2, 4, 3, 5],
#                               [5, 4, 9, 3],
#                               [3, 4, 2, 11],
#                               [10, 9, 13, 15]])
result = Solution().maxMoves([[3, 2, 4],
                              [2, 1, 9],
                              [1, 1, 7]])
print(result)
