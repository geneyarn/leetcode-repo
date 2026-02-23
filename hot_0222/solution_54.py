from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while len(ans) < m * n:
            if top <= bottom:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            if left <= right:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


# result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(result)
