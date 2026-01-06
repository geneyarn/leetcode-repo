from cmath import inf
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        m = len(nums)
        preSum = [0] * (m + 1)
        for i in range(1, m + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        dp = [-inf] * (m + 1)
        dp[k] = preSum[k]

        for i in range(k + 1, m + 1):
            dp[i] = max(dp[i - k] + preSum[i] - preSum[i - k], preSum[i] - preSum[i - k])
        return max(dp)


result = Solution().maxSubarraySum([1, 2], 1)
# result = Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4)
print(result)
