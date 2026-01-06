from functools import cache


class Solution:

    def countHousePlacements(self, n: int) -> int:
        @cache
        def dp(idx: int) -> int:
            if idx == 0:
                return 1
            if idx == 1:
                return 2

            return dp(idx - 1) + dp(idx - 2)

        v = dp(n)
        return (v * v) % (10 ** 9 + 7)


# result = Solution().countHousePlacements(1)
result = Solution().countHousePlacements(2)
print(result)
