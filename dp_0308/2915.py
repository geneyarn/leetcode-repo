from cmath import inf
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
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

        return dp[-1][-1] if dp[-1][-1] > 0 else -1


# result = Solution().lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9)
result = Solution().lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3)
print(result)
