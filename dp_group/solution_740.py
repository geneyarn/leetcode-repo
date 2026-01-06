from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0] * (10 ** 4 + 1)
        for n in nums:
            arr[n] += n

        dp = [0] * (10 ** 4 + 1)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

        return dp[-1]


# result = Solution().deleteAndEarn([3, 4, 2])
result = Solution().deleteAndEarn([2, 2, 3, 3, 3, 4])
print(result)
