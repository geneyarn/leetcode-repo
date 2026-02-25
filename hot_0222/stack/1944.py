from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        m = len(heights)

        ans = [0] * m
        stk = []
        for i in range(m - 1, -1, -1):
            count = 0
            while stk and stk[-1] < heights[i]:
                stk.pop()
                count += 1

            ans[i] = count if not stk else count + 1
            stk.append(heights[i])

        return ans
