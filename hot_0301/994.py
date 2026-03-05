from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        fresh = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time = 0
        while q and fresh > 0:
            sz = len(q)
            time += 1
            for i in range(sz):
                i, j = q.pop(0)
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    q.append((i - 1, j))
                    fresh -= 1
                    grid[i - 1][j] = 2
                if i + 1 < m and grid[i + 1][j] == 1:
                    q.append((i + 1, j))
                    fresh -= 1
                    grid[i + 1][j] = 2

                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    q.append((i, j - 1))
                    fresh -= 1
                    grid[i][j - 1] = 2
                if j + 1 < n and grid[i][j + 1] == 1:
                    q.append((i, j + 1))
                    fresh -= 1
                    grid[i][j + 1] = 2

        return time if fresh == 0 else -1


result = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(result)
