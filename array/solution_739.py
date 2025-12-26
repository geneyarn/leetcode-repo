from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()

            res[i] = stk[-1] - i if stk else 0
            stk.append(i)

        return res


result = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(result)
