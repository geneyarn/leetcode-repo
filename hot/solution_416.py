from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [[False] * (target + 1) for _ in range(m)]

        for i in range(m):
            dp[i][0] = True

        for i in range(m):
            for j in range(1, target + 1):
                if j - nums[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp[-1][-1]


# result = Solution().canPartition([1, 5, 11, 5])
# result = Solution().canPartition([1, 2, 3, 5])
result = Solution().canPartition([1, 2, 5])
print(result)
