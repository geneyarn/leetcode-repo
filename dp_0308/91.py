from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 1

            if s[i] == '0':
                return 0

            ans = dp(i + 1)
            if i + 1 < m and '10' <= s[i:i + 2] <= '26':
                ans += dp(i + 2)

            return ans

        res = dp(0)
        dp.cache_clear()
        return res


result = Solution().numDecodings('12')
print(result)
