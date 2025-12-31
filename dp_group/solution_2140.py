from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(idx: int) -> int:
            if idx >= len(questions):
                return 0
            return max(dp(idx + 1), dp(idx + questions[idx][1] + 1) + questions[idx][0])

        return dp(0)


result = Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])
print(result)
