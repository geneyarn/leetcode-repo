from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False



result = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30)
print(result)
