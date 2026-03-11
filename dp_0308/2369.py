from functools import cache
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        m = len(nums)

        @cache
        def dp(i: int) -> bool:
            if i == m:
                return True

            ans = False
            if i + 1 < m and nums[i + 1] == nums[i]:
                ans = dp(i + 2)
            if i + 2 < m and nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]:
                ans = ans or dp(i + 3)

            if i + 2 < m and nums[i + 1] - nums[i] == 1 and nums[i + 2] - nums[i + 1] == 1:
                ans = ans or dp(i + 3)

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans


# result = Solution().validPartition([4, 4, 4, 5, 6])
# result = Solution().validPartition([1, 1, 1, 2])
# result = Solution().validPartition([865579, 865579, 893593])
result = Solution().validPartition([3, 2, 1])
print(result)
