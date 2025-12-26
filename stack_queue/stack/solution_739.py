from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m = len(temperatures)
        stk = []
        res = [0] * m

        for i in range(m - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()

            res[i] = 0 if not stk else stk[-1] - i
            stk.append(i)
        return res


result = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
# [1, 1, 4, 2, 1, 1, 0, 0]
print(result)
