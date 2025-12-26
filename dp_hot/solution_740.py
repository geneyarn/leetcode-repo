from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)
        arr = [0] * (mx + 1)
        for n in nums:
            arr[n] += n

        dp = [0] * (mx + 1)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, mx + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

        return dp[-1]


result = Solution().deleteAndEarn([3, 4, 2])
print(result)
