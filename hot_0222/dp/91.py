from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(idx: int) -> int:
            if idx == m:
                return 1

            if s[idx] == '0':
                return 0

            ans = dp(idx + 1)

            if idx + 1 < m and '10' <= s[idx:idx + 2] <= '26':
                ans += dp(idx + 2)

            return ans

        ans = dp(0)
        dp.cache_clear()
        return ans


result = Solution().numDecodings('12')
print(result)
