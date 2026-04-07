from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def traverse(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    traverse(i, j)

        return ans
