from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = len(heights)
        left = [-1] * m
        right = [m] * m

        stk = []
        for i in range(m):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()

            left[i] = -1 if not stk else stk[-1]
            stk.append(i)
        stk = []
        for i in range(m - 1, -1, -1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()

            right[i] = stk[-1] if stk else m
            stk.append(i)

        res = 0
        for i in range(m):
            res = max(res, (right[i] - left[i] - 1) * heights[i])

        return res


result = Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
print(result)
