from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        @cache
        def dp(length: int) -> int:
            if length == 0:
                return 1
            ans = 0
            if length - zero >= 0:
                ans += dp(length - zero)
            if length - one >= 0:
                ans += dp(length - one)

            return ans

        return sum(dp(i) for i in range(low, high + 1)) % (10 ** 9 + 7)


result = Solution().countGoodStrings(3, 3, 1, 1)
print(result)
