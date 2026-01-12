from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        m = len(nums)

        @cache
        def dp(i: int, l: int) -> float:
            if i < 0:
                return 0
            ans = 0
            if l == 1:
                ans = sum(nums[:i + 1]) / (i + 1)
            else:
                s = 0

                for j in range(i, -1, -1):
                    s += nums[j]
                    tmp = s / (i - j + 1) + dp(j - 1, l - 1)
                    ans = max(ans, tmp)
            return ans

        result = dp(m - 1, k)
        dp.cache_clear()
        return result


result = Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3)
# result = Solution().largestSumOfAverages([9, 1, 2], 2)
print(result)
