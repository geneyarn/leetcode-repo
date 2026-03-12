from functools import cache
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 1
            big = small = nums[i]
            ans = dp(i + 1)
            for j in range(i + 1, m):
                big = max(big, nums[j])
                small = min(small, nums[j])

                if big - small <= k:
                    ans += dp(j + 1)
                else:
                    break

            return ans

        res = dp(0)
        dp.cache_clear()
        return res % (10 ** 9 + 7)


# result = Solution().countPartitions([9, 4, 1, 3, 7], 4)
result = Solution().countPartitions([3, 3, 4], 0)
print(result)
