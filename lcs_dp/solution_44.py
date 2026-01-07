class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dp(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True

            if i < m and j >= n:
                return False

            if s[i] == p[j] or p[j] == '?':
                return dp(i + 1, j + 1)
            if p[j] == '*':
                return dp(i + 1, j + 1) or dp(i, j + 1)
