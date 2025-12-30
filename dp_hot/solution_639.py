from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(idx: int) -> int:
            if idx == len(s):
                return 1
            c = s[idx]
            if c == '0':
                return 0
            ans = 0
            if c != '*':
                ans += dp(idx + 1)
                if idx + 1 < len(s):
                    if s[idx + 1] == '*' and '1' == s[idx]:
                        ans += 9 * dp(idx + 2)
                    elif s[idx + 1] == '*' and '2' == s[idx]:
                        ans += 6 * dp(idx + 2)
                    elif '10' <= s[idx] + s[idx + 1] <= '26':
                        ans += dp(idx + 2)
            else:
                ans += 9 * dp(idx + 1)
                if idx + 1 < len(s) and '0' <= s[idx + 1] <= '6':
                    ans += 2 * dp(idx + 2)
                elif idx + 1 < len(s) and '7' <= s[idx + 1] <= '9':
                    ans += 1 * dp(idx + 2)
                elif idx + 1 < len(s) and s[idx + 1] == '*':
                    ans += 15 * dp(idx + 2)

            return ans

        return dp(0) % mod


# result = Solution().numDecodings('*')
# result = Solution().numDecodings('1*')
# result = Solution().numDecodings('2*')
# result = Solution().numDecodings('**')
# result = Solution().numDecodings("*7")
# result = Solution().numDecodings("1*72*")
result = Solution().numDecodings("*********")
# 15 * 9 + 2 * 15
print(result)
