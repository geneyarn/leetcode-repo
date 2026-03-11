from functools import cache


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        m = len(s)

        @cache
        def valid(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0
            # ans = dp(i + 1)
            ans = 0
            for j in range(i + k, m + 1):
                if valid(i, j - 1):
                    ans = max(ans, 1 + dp(j))
                    break
            ans = max(ans, dp(i + 1))

            return ans

        res = dp(0)
        valid.cache_clear()
        dp.cache_clear()

        return res


# result = Solution().maxPalindromes('abaccdbbd', 3)
result = Solution().maxPalindromes('adbcda', 2)
print(result)
