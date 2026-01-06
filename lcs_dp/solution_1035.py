from functools import cache
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if nums1[i] == nums2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


result = Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4])
print(result)
