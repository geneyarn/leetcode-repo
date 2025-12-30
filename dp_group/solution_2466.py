import math


class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]

        ans = 0
        for i in range(low, high + 1):
            ans += dp[i]
        return ans % int(math.pow(10, 9) + 7)


# result = Solution().countGoodStrings(3, 3, 1, 1)
result = Solution().countGoodStrings(2, 3, 1, 2)
print(result)
