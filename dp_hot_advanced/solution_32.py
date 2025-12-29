class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        dp = [0] * (m + 1)
        stk = []

        for i in range(1, m + 1):
            c = s[i - 1]
            if c == '(':
                stk.append(i)
                dp[i] = 0
            else:
                if not stk:
                    dp[i] = 0
                else:
                    left = stk.pop()
                    dp[i] = dp[left - 1] + (i - left + 1)
        return max(dp)


# result = Solution().longestValidParentheses('(()')
result = Solution().longestValidParentheses(')()())')
print(result)
