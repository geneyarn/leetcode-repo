from math import inf
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        big = [[-inf] * n for _ in range(m)]
        small = [[inf] * n for _ in range(m)]
        big[0][0] = small[0][0] = grid[0][0]
        for i in range(1, m):
            big[i][0] = big[i - 1][0] * grid[i][0]
            small[i][0] = small[i - 1][0] * grid[i][0]

        for j in range(1, n):
            big[0][j] = big[0][j - 1] * grid[0][j]
            small[0][j] = small[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                big[i][j] = max(big[i - 1][j] * grid[i][j], big[i][j - 1] * grid[i][j],
                                small[i - 1][j] * grid[i][j], small[i][j - 1] * grid[i][j])
                small[i][j] = min(big[i - 1][j] * grid[i][j], big[i][j - 1] * grid[i][j],
                                  small[i - 1][j] * grid[i][j], small[i][j - 1] * grid[i][j])

        return big[-1][-1] % (10 ** 9 + 7) if big[-1][-1] >= 0 else -1


# result = Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]])
result = Solution().maxProductPath([[1, 3], [0, -4]])
# result = Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]])
print(result)
