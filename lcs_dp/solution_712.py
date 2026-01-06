from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 and j < 0:
                return 0

            if j < 0 and i >= 0:
                ans = 0
                for k in range(i, -1, -1):
                    ans += ord(s1[k])
                return ans
            if i < 0 and j >= 0:
                ans = 0
                for k in range(j, -1, -1):
                    ans += ord(s2[k])
                return ans

            if s1[i] == s2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i - 1, j) + ord(s1[i]), dp(i, j - 1) + ord(s2[j]))

        ans = dp(m - 1, n - 1)
        dp.cache_clear()
        return ans


result = Solution().minimumDeleteSum('sea', 'eat')
print(result)
print(ord('a'))
