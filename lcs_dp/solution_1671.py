from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        pre = self.getLISArray(nums)
        suf = self.getLISArray(nums[::-1])[::-1]
        ans = 1
        for v1, v2 in zip(pre, suf):
            if v1 > 1 and v2 > 1:
                ans = max(ans, v1 + v2 - 1)
        return len(nums) - ans

    def getLISArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp


result = Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1])
