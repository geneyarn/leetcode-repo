from functools import cache


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 1
            ans = 0
            for j in range(i, max(i - 10, -1), -1):
                if s[j] == '0':
                    continue
                sub = int(s[j:i + 1])
                if 1 <= sub <= k:
                    tmp = dp(j - 1)
                    if tmp > 0:
                        ans += tmp
            return ans

        result = dp(m - 1)
        dp.cache_clear()
        return result % (10 ** 9 + 7)


# result = Solution().numberOfArrays('1000', 1000)
# result = Solution().numberOfArrays('1000', 10)
# result = Solution().numberOfArrays('1317', 2000)
# result = Solution().numberOfArrays('2020', 30)
result = Solution().numberOfArrays('1234567890', 90)
print(result)
