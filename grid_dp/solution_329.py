from functools import cache
from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, columns = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @cache
        def dfs(row: int, column: int) -> int:
            ans = 1
            for dx, dy in dirs:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    ans = max(ans, dfs(newRow, newColumn) + 1)
            return ans

        result = 1
        for r in range(rows):
            for c in range(columns):
                result = max(result, dfs(r, c))
        return result


r = Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
print(r)
