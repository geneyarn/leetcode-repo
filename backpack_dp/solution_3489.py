from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        m = len(queries)
        for idx, n in enumerate(nums):
            if n == 0:
                continue
            dp = [[False] * (n + 1) for _ in range(m + 1)]
            dp[0][0] = True
            for i in range(1, m + 1):
                query = queries[i - 1]
                for j in range(n + 1):
                    if not (query[0] <= idx <= query[1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        if j - query[2] >= 0:
                            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - query[2]]
                        else:
                            dp[i][j] = dp[i - 1][j]
                if dp[i][n]:
                    break
            if i == m and not dp[i][n]:
                return -1
            ans = max(ans, i)
        return ans


# result = Solution().minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]])
result = Solution().minZeroArray([1, 2, 3, 2, 1], [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 4, 1]])
print(result)
