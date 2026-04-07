from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, n - 1
        t, b = 0, m - 1

        ans = []

        while len(ans) < m * n:
            if t <= b:
                for i in range(l, r + 1):
                    ans.append(matrix[t][i])
                t += 1
            if l <= r:
                for i in range(t, b + 1):
                    ans.append(matrix[i][r])
                r -= 1

            if t <= b:
                for i in range(r, l - 1, - 1):
                    ans.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1

        return ans


# result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(result)
