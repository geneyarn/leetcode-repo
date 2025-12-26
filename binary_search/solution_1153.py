from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1
        ans = 0
        while 0 <= i < m and 0 <= j and n:
            if grid[i][j] >= 0:
                i += 1
            else:
                ans += (m - i)
                j -= 1

        print(str(i) + '{i}----{j}' + str(j))

        return ans


result = Solution().countNegatives([[4, 3, 2, -1],
                                    [3, 2, 1, -1],
                                    [1, 1, -1, -2],
                                    [-1, -1, -2, -3]])
print(result)
