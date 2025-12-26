from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n - 1

        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False
