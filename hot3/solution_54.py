from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []

        up, down = 0, m - 1
        left, right = 0, n - 1
        while len(ans) < m * n:
            if up <= down:
                for i in range(left, right + 1):
                    ans.append(matrix[up][i])
                up += 1
            if left <= right:
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if up <= down:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
