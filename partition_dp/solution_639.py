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
            ans = 0
            if s[i] == '*':
                ans += 9 * dp(i + 1)
                if i + 1 < m and '0' <= s[i + 1] <= '6':
                    ans += 2 * dp(i + 2)
                if i + 1 < m and '7' <= s[i + 1] <= '9':
                    ans += dp(i + 2)
                if i + 1 < m and s[i + 1] == '*':
                    ans += 15 * dp(i + 2)
            else:
                ans += dp(i + 1)
                if i + 1 < m and s[i + 1] != '*' and '10' <= s[i:i + 2] <= '26':
                    ans += dp(i + 2)
                if i + 1 < m and s[i + 1] == '*' and '1' == s[i]:
                    ans += 9 * dp(i + 2)
                if i + 1 < m and s[i + 1] == '*' and s[i] == '2':
                    ans += 6 * dp(i + 2)
            return ans

        result = dp(0)
        dp.cache_clear()
        return result % (10 ** 9 + 7)


# result = Solution().numDecodings('*')
# result = Solution().numDecodings('1*')
# result = Solution().numDecodings('2*')
# result = Solution().numDecodings('*1')  # 9 +
# result = Solution().numDecodings('*7')  # 9 +
result = Solution().numDecodings('**')  # 9 +
print(result)
