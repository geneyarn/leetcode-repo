from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        mx = max(power)
        arr = [0] * (mx + 1)
        for n in power:
            arr[n] += n

        if len(arr) <= 3:
            return max(arr)

        dp = [0] * (mx + 1)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        dp[2] = max(arr[0], arr[1], arr[2])
        for i in range(3, len(arr)):
            dp[i] = max(dp[i - 1], dp[i - 2], dp[i - 3] + arr[i])

        return dp[-1]


# result = Solution().maximumTotalDamage([1, 1, 3, 4])
# result = Solution().maximumTotalDamage([7, 1, 6, 6])
result = Solution().maximumTotalDamage([1, 1, 1, 1, 1, 1])
print(result)
