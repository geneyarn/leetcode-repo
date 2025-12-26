from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        mx = 0
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    mx = max(mx, dp[i][j])
        return mx * mx

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        mx = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    mx = max(mx, dp[i][j])

        return mx * mx


result = Solution().maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]])
# result = Solution().maximalSquare(
#     [["0", "1"],
#      ["1", "0"]])

print(result)
