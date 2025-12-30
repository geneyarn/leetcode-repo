class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        dp = [[False] * (m) for _ in range(m)]
        for i in range(m):
            dp[i][i] = True
        mxLen = 1
        start = 0
        for i in range(m - 2, -1, -1):
            for j in range(i + 1, m):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 1):
                    dp[i][j] = True
                    if j - i + 1 >= mxLen:
                        start = i
                        mxLen = j - i + 1

        return s[start:start + mxLen]


# result = Solution().longestPalindrome('babad')
result = Solution().longestPalindrome('cbbd')
print(result)
