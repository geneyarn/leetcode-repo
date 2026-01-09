from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(scores, ages))

        dp = [0] * len(arr)
        ans = 0
        for i in range(len(arr)):
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], dp[j])

            dp[i] += arr[i][0]
            ans = max(ans, dp[i])
        return ans


result = Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5])
print(result)
