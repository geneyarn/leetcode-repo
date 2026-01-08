from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # p[j] = . or p[j] = s[i] f(i, j) = f(i + 1, j + 1)
        # p[j] != s[i] and p[j + 1] = '*'  f(i, j) = f(i, j + 2)
        @cache
        def dp(i: int, j: int) -> bool:
            if j >= n:
                return i >= m

            # j < n
            if i >= m:
                remain = n - j
                if remain % 2 != 0:
                    return False
                for k in range(j + 1, n, 2):
                    if p[k] != '*':
                        return False

                return True

            # j < n and i < m
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n and p[j + 1] == '*':
                    #      match one char        match zero char
                    return dp(i + 1, j) or dp(i, j + 2)
                else:
                    return dp(i + 1, j + 1)
            else:
                if j + 1 < n and p[j + 1] == '*':
                    return dp(i, j + 2)
                else:
                    return False

        result = dp(0, 0)
        dp.cache_clear()
        return result


r = Solution().isMatch('aa', 'a')
# r = Solution().isMatch('aa', 'a*')
# r = Solution().isMatch('ab', '.*')
print(r)
