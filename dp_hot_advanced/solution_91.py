from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        m = len(s)

        @cache
        def dp(idx: int) -> int:
            if idx == m:
                return 1

            ans = 0
            if s[idx] == '0':
                return 0
            ans += dp(idx + 1)
            if idx + 1 < m:
                v = s[idx] + s[idx + 1]
                if '10' <= v <= '26':
                    ans += dp(idx + 2)

            return ans


        return dp(0)

result = Solution().numDecodings('12')
print(result)
