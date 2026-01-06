from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if word1[i] == word2[j]:
                return 1 + dp(i - 1, j - 1)
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        common = dp(m - 1, n - 1)
        dp.cache_clear()
        return len(word1) + len(word2) - 2 * common


result = Solution().minDistance('sea', 'eat')
print(result)
