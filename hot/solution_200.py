from typing import List


class Solution:

    def traverse(self, grid: List[List[str]], i: int, j: int):
        if i >= len(grid) or i < 0:
            return
        if j >= len(grid[i]) or j < 0:
            return

        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.traverse(grid, i - 1, j)
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i, j - 1)
        self.traverse(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ans += 1
                    self.traverse(grid, i, j)

        return ans


result = Solution().numIslands([["1", "0", "1", "1", "0", "1", "1"]])
print(result)
