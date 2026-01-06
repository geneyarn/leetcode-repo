from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [m + 1] * m
        dp[m - 1] = 0
        for i in range(m - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                dp[i] = min(dp[i], dp[min(i + j, m - 1)] + 1)

        return dp[0]


# result = Solution().jump([2, 3, 1, 1, 4])
result = Solution().jump([2, 3, 0, 1, 4])
print(result)
