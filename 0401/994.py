from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

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

                for ii, jj in directions:
                    newI, newJ = i + ii, j + jj
                    if 0 <= newI < m and 0 <= newJ < n:
                        if grid[newI][newJ] == 1:
                            fresh -= 1
                            grid[newI][newJ] = 2
                            q.append((newI, newJ))

        return ans if fresh == 0 else -1


# result = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
result = Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
print(result)
