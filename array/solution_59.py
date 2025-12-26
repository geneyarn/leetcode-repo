from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        upper = 0
        lower = n - 1
        left = 0
        right = n - 1
        num = 1
        while num <= n * n:
            if upper <= lower:
                for i in range(left, right + 1):
                    res[upper][i] = num
                    num += 1
                upper += 1
            if left <= right:
                for i in range(upper, lower + 1):
                    res[i][right] = num
                    num += 1
                right -= 1

            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res[lower][i] = num
                    num += 1
                lower -= 1

            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res[i][left] = num
                    num += 1
                left += 1

        return res


result = Solution().generateMatrix(3)
print(result)

# [[1,2,3],[8,9,4],[7,6,5]]
