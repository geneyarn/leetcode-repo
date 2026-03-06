class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        dp = [0] * (m + 1)

        stk = []
        for i in range(1, m + 1):
            c = s[i - 1]
            if c == ')':
                if not stk:
                    dp[i] = 0
                else:
                    lastIdx = stk.pop()
                    dp[i] = dp[lastIdx - 1] + (i - lastIdx + 1)
            else:
                stk.append(i)

        return max(dp)


# result = Solution().longestValidParentheses('(()')
result = Solution().longestValidParentheses(')()())')
print(result)
