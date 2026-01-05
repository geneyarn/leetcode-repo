from functools import cache
from typing import List


class Solution:
    def __init__(self):
        self.ans = 0

    def countPaths(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @cache
        def dfs(row: int, column: int) -> int:

            ans = 1

            for p in dirs:
                newRow, newColumn = row + p[0], column + p[1]
                if 0 <= newRow < rows and 0 <= newColumn < columns and grid[newRow][newColumn] > grid[row][column]:
                    ans += dfs(newRow, newColumn)
            return ans

        result = 0
        for i in range(rows):
            for j in range(columns):
                result += dfs(i, j)
        return result


result = Solution().countPaths([[1, 1], [3, 4]])
print(result)
