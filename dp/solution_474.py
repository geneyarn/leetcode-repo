from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]

        for i in range(1, l + 1):
            one = strs[i - 1].count('1')
            zero = strs[i - 1].count('0')

            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zero and k >= one:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero][k - one] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[-1][-1][-1]


# result = Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
result = Solution().findMaxForm(["10", "0", "1"], 1, 1)
print(result)
