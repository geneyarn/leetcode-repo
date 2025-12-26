from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1] * m

        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


result = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
# result = Solution().lengthOfLIS([0, 1, 0, 3, 2, 3])
print(result)
