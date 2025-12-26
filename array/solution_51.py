from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def valid(self, grid: List[List[str]], row: int, col: int) -> bool:

        for r in range(len(grid)):
            if grid[r][col] == 'Q':
                return False

        i, j = row - 1, col - 1

        while i >= 0 and j >= 0:
            if grid[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < len(grid):
            if grid[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backTrack(self, grid: List[List[str]], row: int):
        if row >= len(grid):
            tmp = []
            for row in grid:
                tmp.append(''.join(row))
            self.res.append(tmp)
            return

        for i in range(len(grid)):
            if not self.valid(grid, row, i):
                continue
            grid[row][i] = 'Q'
            self.backTrack(grid, row + 1)
            grid[row][i] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]
        self.backTrack(grid, 0)

        return self.res


result = Solution().solveNQueens(4)
print(result)
