from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return -inf

            ans1 = nums1[i] * nums2[j] + max(dp(i - 1, j - 1), 0)
            ans2 = dp(i - 1, j)
            ans3 = dp(i, j - 1)

            return max(ans1, ans2, ans3)

        result = dp(m - 1, n - 1)
        dp.cache_clear()
        return result


result = Solution().maxDotProduct([2, 1, -2, 5], [3, 0, -6])
print(result)
