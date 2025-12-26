class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        dp = [[False] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = True
        start = 0
        length = 1
        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 2):
                    dp[i][j] = True
                    if j - i + 1 > length:
                        start = i
                        length = j - i + 1
        return s[start: start + length]


result = Solution().longestPalindrome('babad')
print(result)
