from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        m = len(arr)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0
            mx = 0
            ans = 0
            for j in range(i, min(i + k, m)):
                mx = max(mx, arr[j])
                ans = max(ans, (j - i + 1) * mx + dp(j + 1))
            return ans

        result = dp(0)
        dp.cache_clear()
        return result


result = Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)
print(result)
