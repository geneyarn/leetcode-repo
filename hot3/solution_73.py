from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row = [False] * m
        column = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    column[j] = row[i] = True

        for i in range(m):
            for j in range(n):
                if row[i] or column[j]:
                    matrix[i][j] = 0


arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

Solution().setZeroes(arr)
print(arr)
