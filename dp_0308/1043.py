from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        m = len(arr)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0
            ans = dp(i + 1) + arr[i]
            big = arr[i]

            for j in range(i + 1, min(i + k, m)):
                big = max(arr[j], big)

                ans = max(ans, dp(j + 1) + big * (j - i + 1))

            return ans

        res = dp(0)
        dp.cache_clear()
        return res


# result = Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)
result = Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4)
print(result)
