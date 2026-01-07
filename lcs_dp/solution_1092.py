from functools import cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        @cache
        def dp(i: int, j: int) -> str:
            if i < 0:
                return str2[:j + 1]
            if j < 0:
                return str1[:i + 1]

            if str1[i] == str2[j]:
                return dp(i - 1, j - 1) + str1[i]

            ans1 = dp(i - 1, j) + str1[i]
            ans2 = dp(i, j - 1) + str2[j]
            return ans1 if len(ans1) < len(ans2) else ans2

        result = dp(m - 1, n - 1)
        dp.cache_clear()
        return result


result = Solution().shortestCommonSupersequence('abac', 'cab')
print(result)
