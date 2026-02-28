from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if matrix[0][0] == '1' else 0
        mx = 0
        for i in range(m):
            if matrix[i][0] == '1':
                mx = 1
                dp[i][0] = 1
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                mx = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    ) + 1
                mx = max(mx, dp[i][j])

        return mx ** 2


result = Solution().maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]])
print(result)
