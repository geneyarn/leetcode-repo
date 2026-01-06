from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i - 1, j - 1)
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


result = Solution().longestCommonSubsequence('abcde', 'ace')
print(result)
