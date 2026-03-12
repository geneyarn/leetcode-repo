from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        m = len(nums)

        @cache
        def dp(i: int, l: int) -> float:
            if i >= m:
                return 0
            if l == 1:
                return sum(nums[i:]) / (m - i)
            else:
                s = 0
                ans = 0
                for j in range(i, m):
                    s += nums[j]

                    avg = s / (j - i + 1)
                    ans = max(ans, avg + dp(j + 1, l - 1))

            return ans

        res = dp(0, k)
        dp.cache_clear()
        return res


result = Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3)
print(result)
