import bisect
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        m = len(arr1)

        @cache
        def dp(i: int, pre: int) -> int:
            if i < 0:
                return 0
            res = dp(i - 1, arr1[i]) if arr1[i] < pre else inf

            k = bisect.bisect_left(arr2, pre) - 1
            if k >= 0:
                res = min(res, dp(i - 1, arr2[k]) + 1)

            return res

        ans = dp(m - 1, inf)
        dp.cache_clear()
        return ans


# result = Solution().makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4])
result = Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1])
print(result)
