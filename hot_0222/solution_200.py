from typing import List


class Solution:

    def __init__(self):
        self.ans = 0

    def traverse(self, grid: List[List[str]], i: int, j: int):
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
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.ans += 1
                    self.traverse(grid, i, j)
        return self.ans


result = Solution().numIslands([
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
])
print(result)
