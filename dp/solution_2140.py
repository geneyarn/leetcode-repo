from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        m = len(questions)

        dp = [0] * (m + 1)

        for i in range(m - 1, -1, -1):
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(m, i + questions[i][1] + 1)])

        return dp[0]


result = Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])
print(result)
