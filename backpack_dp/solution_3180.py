from functools import cache
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        m = len(rewardValues)
        big = 2 * rewardValues[-1] - 1

        maxValue = 0

        @cache
        def dp(i: int, num: int) -> int:
            if i >= m:
                return num

            nonlocal maxValue
            v = rewardValues[i]
            # print(f'{num}----{v}---{num - v}')
            if v > num:
                ans = max(dp(i + 1, num), dp(i + 1, num + v))
            else:
                ans = dp(i + 1, num)
            maxValue = max(ans, maxValue)
            # print(f'{i}---{num}---{ans}')
            return ans

        dp(0, 0)
        dp.cache_clear()
        return maxValue

    def maxTotalReward2(self, rewardValues: List[int]) -> int:
        # rewardValues.sort()

        big = rewardValues[-1] * 2
        m = len(rewardValues)
        dp = [[False] * (big + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            v = rewardValues[i - 1]
            for j in range(big + 1):
                dp[i][j] = dp[i - 1][j]
                if 0 <= j - v < v:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - rewardValues[i - 1]]

        for i in range(big, -1, -1):
            if dp[-1][i]:
                return i

        return 0


# result = Solution().maxTotalReward([1, 1, 3, 3])
result = Solution().maxTotalReward([1, 6, 4, 3, 2])
print(result)
