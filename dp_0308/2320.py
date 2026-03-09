from functools import cache


class Solution:
    def countHousePlacements(self, n: int) -> int:

        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 2

            return dp(i - 1) + dp(i - 2)

        ans = dp(n)
        dp.cache_clear()
        return ans * ans % (10 ** 9 + 7)
