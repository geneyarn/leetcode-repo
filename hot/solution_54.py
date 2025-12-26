from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1
        left, right = 0, n - 1

        res = []
        while len(res) < m * n:
            if top <= bot:
                l = left
                while l <= right:
                    res.append(matrix[top][l])
                    l += 1
                top += 1
            if left <= right:
                t = top
                while t <= bot:
                    res.append(matrix[t][right])
                    t += 1
                right -= 1

            if top <= bot:
                r = right
                while r >= left:
                    res.append(matrix[bot][r])
                    r -= 1
                bot -= 1
            if left <= right:
                b = bot
                while b >= top:
                    res.append(matrix[b][left])
                    b -= 1
                left += 1
        return res


result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
