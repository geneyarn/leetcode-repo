from functools import cache
from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        m = len(energyDrinkA)
        c = [energyDrinkA, energyDrinkB]

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0:
                return 0

            return max(dp(i - 1, j), dp(i - 2, j ^ 1)) + c[j][i]

        ans = max(dp(m - 1, 0), dp(m - 1, 1))
        dp.cache_clear()
        return ans


result = Solution().maxEnergyBoost([4, 1, 1], [1, 1, 3])
print(result)
