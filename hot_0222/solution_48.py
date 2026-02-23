from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)

        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(m):
            j, k = 0, m - 1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(arr)
print(arr)
