from functools import cache
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 1
            if s[i] == '0':
                return 0
            ans = 0
            for j in range(i, m):
                sub = s[i:j + 1]
                if len(sub) > len(str(k)):
                    break
                n = int(sub)

                if 1 <= n <= k:
                    ans += dp(j + 1)
            return ans

        res = dp(0)
        dp.cache_clear()
        return res % (10 ** 9 + 7)


# result = Solution().numberOfArrays('1000', 10000)
# result = Solution().numberOfArrays('1000', 10)
# result = Solution().numberOfArrays('1317', 2000)
result = Solution().numberOfArrays('2020', 30)
print(result)
