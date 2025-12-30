from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dp(curSum: int) -> int:
            if curSum > target:
                return 0
            if curSum == target:
                return 1
            ans = 0
            for i in range(len(nums)):
                curSum += nums[i]
                ans += dp(curSum)
                curSum -= nums[i]
            return ans

        return dp(0)


result = Solution().combinationSum4([1, 2, 3], 4)
print(result)
