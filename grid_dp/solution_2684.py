from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, v: int) -> int:
            if i < 0 or i >= m:
                return -inf
            if j >= n:
                return -inf

            if grid[i][j] <= v:
                return j - 1

            ans = j
            for l in (i - 1, i, i + 1):
                ans = max(ans, dfs(l, j + 1, grid[i][j]))
            print(f'{i}----{j}----{ans}')
            return ans

        return max(dfs(k, 0, -inf) for k in range(m))

        result = 0
        for k in range(m):
            tmp = dfs(k, 0, -inf)
            result = max(result, tmp)
            print(f'+++++{tmp}----{result}')
        return result


result = Solution().maxMoves([[2, 4, 3, 5],
                              [5, 4, 9, 3],
                              [3, 4, 2, 11],
                              [10, 9, 13, 15]])
# result = Solution().maxMoves([[3, 2, 4],
#                               [2, 1, 9],
#                               [1, 1, 7]])
print(result)
