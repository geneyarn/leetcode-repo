from functools import cache


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        m = len(s)

        @cache
        def palindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            return s[i] == s[j] and palindrome(i + 1, j - 1)

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0

            if i + 1 < k:
                return 0
            ans = dp(i - 1)
            for j in range(i - k + 1, -1, -1):
                if not palindrome(j, i):
                    continue

                ans = max(1 + dp(j - 1), ans)
            return ans

        mxLen = dp(m - 1)
        dp.cache_clear()
        palindrome.cache_clear()
        return mxLen


# result = Solution().maxPalindromes('adbcda', 2)
result = Solution().maxPalindromes('abaccdbbd', 3)
print(result)
