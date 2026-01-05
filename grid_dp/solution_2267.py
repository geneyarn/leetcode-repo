from functools import cache
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows, columns = len(grid), len(grid[0])

        if (rows + columns) % 2 == 0 or grid[0][0] == ')' or grid[rows - 1][columns - 1] == '(':
            return False

        @cache
        def dfs(row: int, column: int, leftCount: int) -> bool:
            if row >= rows or column >= columns:
                return False

            if row == rows - 1 and column == columns - 1:
                return leftCount == 1 and grid[row][column] == ')'

            leftCount += (1 if grid[row][column] == '(' else -1)
            tmp = leftCount >= 0 and (dfs(row + 1, column, leftCount) or dfs(row, column + 1, leftCount))

        return dfs(0, 0, 0)


# result = Solution().hasValidPath([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]])
result = Solution().hasValidPath([[")", ")"], ["(", "("]])
print(result)
