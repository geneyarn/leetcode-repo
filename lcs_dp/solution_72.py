from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 and j < 0:
                return 0
            if i < 0 and j >= 0:
                return j + 1
            if i >= 0 and j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


result = Solution().minDistance('horse', 'ros')
print(result)
