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

        ans = 0
        while q and fresh > 0:
            sz = len(q)
            ans += 1
            for i in range(sz):
                i, j = q.pop(0)
                if 0 <= i < m and 0 <= j + 1 < n and grid[i][j + 1] == 1:
                    q.append((i, j + 1))
                    grid[i][j + 1] = 2
                    fresh -= 1
                if 0 <= i < m and 0 <= j - 1 < n and grid[i][j - 1] == 1:
                    q.append((i, j - 1))
                    grid[i][j - 1] = 2
                    fresh -= 1
                if 0 <= i + 1 < m and 0 <= j < n and grid[i + 1][j] == 1:
                    q.append((i + 1, j))
                    grid[i + 1][j] = 2
                    fresh -= 1
                if 0 <= i - 1 < m and 0 <= j < n and grid[i - 1][j] == 1:
                    q.append((i - 1, j))
                    grid[i - 1][j] = 2
                    fresh -= 1

        return ans if fresh == 0 else -1


result = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(result)
