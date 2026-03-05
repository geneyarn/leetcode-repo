from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m = len(temperatures)
        ans = [0] * m
        stk = []

        for i in range(m - 1, -1, -1):
            n = temperatures[i]

            while stk and temperatures[stk[-1]] <= n:
                stk.pop()
            ans[i] = 0 if not stk else stk[-1] - i

            stk.append(i)

        return ans


result = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(result)
