from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        leftMax, rightMax = height[0], height[-1]
        i, j = 0, m - 1

        res = 0
        while i < j:
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])
            res = max(res, min(leftMax, rightMax) * (j - i))
            if leftMax < rightMax:
                i += 1
            else:
                j -= 1
        return res
