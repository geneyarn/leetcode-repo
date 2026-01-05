from functools import cache
from math import inf
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        m = len(nums)

        @cache
        def dp(i: int, num: int) -> int:
            if i < 0:
                return 0 if num == 0 else -inf
            v = nums[i]
            if num >= v:
                return max(dp(i - 1, num), dp(i - 1, num - v) + 1)
            else:
                return dp(i - 1, num)

        ans = dp(m - 1, target)
        dp.cache_clear()
        return ans if ans > -inf else -1

    def lengthOfLongestSubsequence2(self, nums: List[int], target: int) -> int:
        m = len(nums)
        dp = [[-inf] * (target + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            v = nums[i - 1]
            for j in range(target + 1):
                if j >= v:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] if dp[-1][-1] > -inf else -1


# result = Solution().lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9)
result = Solution().lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7)
# result = Solution().lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3)
print(result)
