from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        upper, lower = 0, m - 1
        left, right = 0, n - 1

        while len(res) < m * n:
            if upper <= lower:
                for i in range(left, right + 1):
                    res.append(matrix[upper][i])
                upper += 1

            if left <= right:
                for i in range(upper, lower + 1):
                    res.append(matrix[i][right])
                right -= 1

            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res.append(matrix[lower][i])
                lower -= 1

            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


# result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = Solution().spiralOrder([[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12]])
print(result)
# [1,2,3,6,9,8,7,4,5]
