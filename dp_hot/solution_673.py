from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1] * len(nums)
        dp[0] = 1
        cnt = [1] * m

        mx = 1
        for i in range(1, m):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
                mx = max(mx, dp[i])

        res = 0
        for i in range(m):
            if dp[i] == mx:
                res += cnt[i]

        return res


result = Solution().findNumberOfLIS([1, 3, 5, 4, 7])
# result = Solution().findNumberOfLIS([2, 2, 2, 2, 2])
print(result)
