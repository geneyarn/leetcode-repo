from functools import cache


class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        s = str(ciphertext)
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 1

            ans = dp(i + 1)
            if i + 1 < m and '10' <= s[i:i + 2] <= '25':
                ans += dp(i + 2)

            return ans

        result = dp(0)
        dp.cache_clear()
        return result


result = Solution().crackNumber(216612)
print(result)
