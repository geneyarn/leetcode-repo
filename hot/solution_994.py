from typing import List


# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        q = []

        fresh = 0
        for i in range(m):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        res = 0

        while q and fresh > 0:
            l = len(q)
            for i in range(l):
                a = q.pop(0)
                if a[0] - 1 >= 0 and grid[a[0] - 1][a[1]] == 1:
                    grid[a[0] - 1][a[1]] = 2
                    q.append([a[0] - 1, a[1]])
                if a[0] + 1 < m and grid[a[0] + 1][a[1]] == 1:
                    grid[a[0] + 1][a[1]] = 2
                    q.append([a[0] + 1, a[1]])
                if a[1] - 1 >= 0 and grid[a[0]][a[1] - 1] == 1:
                    grid[a[0]][a[1] - 1] = 2
                    q.append([a[0], a[1] - 1])
                if a[1] + 1 < len(grid[a[0]]) and grid[a[0]][a[1] + 1] == 1:
                    grid[a[0]][a[1] + 1] = 2
                    q.append([a[0], a[1] + 1])
            if len(q) > 0:
                fresh -= len(q)
                res += 1

        return res if fresh == 0 else -1


# result = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
# result = Solution().orangesRotting([[0, 2]])
result = Solution().orangesRotting([[0]])
print(result)
