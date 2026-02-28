from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1] * m
        cnt = [1] * m

        mx = 1
        for i in range(m):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]

                    mx = max(mx, cnt[i])
        ans = 0
        for n in cnt:
            if n == mx:
                ans += n

        return ans


resutl = Solution().findNumberOfLIS([1, 3, 5, 4, 7])
print(resutl)
