from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        m = len(rewardValues)

        mx = rewardValues[-1]

        dp = [[False] * (2 * mx + 1) for _ in range(m + 1)]
        dp[0][0] = True

        ans = 0

        for i in range(1, m + 1):
            v = rewardValues[i - 1]

            for j in range(2 * mx + 1):
                if j >= v and v > j - v:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - v]
                else:
                    dp[i][j] = dp[i - 1][j]

                if dp[i][j]:
                    ans = max(ans, j)

        return ans


result = Solution().maxTotalReward([1, 6, 4, 3, 2])
print(result)
