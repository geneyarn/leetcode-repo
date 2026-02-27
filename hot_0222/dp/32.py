class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        dp = [0] * (m + 1)

        mp = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stk = []
        for i in range(1, m + 1):
            c = s[i - 1]
            if c in mp:
                if not stk or mp[c] != s[stk[-1] - 1]:
                    dp[i] = 0
                else:
                    idx = stk.pop()
                    dp[i] = dp[idx - 1] + (i - idx + 1)
            else:
                stk.append(i)

        return max(dp)


result = Solution().longestValidParentheses('(()')
# result = Solution().longestValidParentheses(')()())')
print(result)
