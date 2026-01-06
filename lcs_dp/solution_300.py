from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)

        def dp(i: int) -> int:
            ans = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp(j) + 1)
            return ans

        return max([dp(k) for k in range(m)])

    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]


result = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(result)
