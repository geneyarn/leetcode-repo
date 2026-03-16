from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        m = len(nums)

        dp = [1] * m
        count = [1] * m

        mx = 1
        for i in range(1, m):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]

            mx = max(mx, dp[i])

        ans = 0
        for i in range(m):
            if dp[i] == mx:
                ans += count[i]

        return ans


result = Solution().findNumberOfLIS([1, 3, 5, 4, 7])
print(result)
