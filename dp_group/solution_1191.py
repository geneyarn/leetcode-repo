from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        m = len(arr)
        # dp = [0] * (m * k + 1)
        cur = 0
        ma = 0
        for i in range(1, m * k + 1):
            # dp[i] = max(dp[i - 1] + arr[(i - 1) % m], arr[(i - 1) % m])
            # dp[i] = max(dp[i - 1] + arr[(i - 1) % m], arr[(i - 1) % m])
            cur = max(cur + arr[(i - 1) % m], arr[(i - 1) % m])
            ma = max(ma, cur)

        return max(ma, 0) % (10 ** 9 + 7)


# result = Solution().kConcatenationMaxSum([1, 2], 3)
result = Solution().kConcatenationMaxSum([1, -2, 1], 5)
print(result)
