class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        stk = []

        dp = [0] * (m + 1)

        for i in range(1, m + 1):
            c = s[i - 1]
            if c == '(':
                dp[i] = 0
                stk.append(i)
            else:
                if not stk:
                    dp[i] = 0
                else:
                    last = stk.pop()
                    dp[i] = dp[last - 1] + (i - last + 1)

        return max(dp)
