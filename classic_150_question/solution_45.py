from functools import cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [m] * m
        dp[0] = 0

        for i in range(m):
            for j in range(1, nums[i] + 1):
                if i + j < m:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]


    def jump2(self, nums: List[int]) -> int:
        m = len(nums)

        @cache
        def dp(idx: int) -> int:
            if idx >= m - 1:
                return 0
            res = 10001
            for i in range(1, nums[idx] + 1):
                res = min(res, dp(idx + i) + 1)
            return res

        return dp(0)

result = Solution().jump([2,3,1,1,4])
print(result)
