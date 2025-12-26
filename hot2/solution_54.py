from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        l, r = 0, n - 1
        u, d = 0, m - 1

        while len(res) < m * n:
            if u <= d:
                for i in range(l, r + 1):
                    res.append(matrix[u][i])
                u += 1

            if l <= r:
                for i in range(u, d + 1):
                    res.append(matrix[i][r])
                r -= 1

            if u <= d:
                for i in range(r, l - 1, - 1):
                    res.append(matrix[d][i])
                d -= 1
            if l <= r:
                for i in range(d, u - 1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res


result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
