from typing import List


class Solution:

    def traverse(self, grid: list[list[str]], i: int, j: int):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i - 1, j)
        self.traverse(grid, i, j + 1)
        self.traverse(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.traverse(grid, i, j)

        return ans
