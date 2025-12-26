from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        lMax = [0] * m
        lMax[0] = height[0]

        for i in range(1, m):
            lMax[i] = max(lMax[i - 1], height[i])

        rMax = [0] * m
        rMax[-1] = height[-1]
        for i in range(m - 2, -1, -1):
            rMax[i] = max(rMax[i + 1], height[i])

        res = 0
        for i in range(m):
            res += min(lMax[i], rMax[i]) - height[i]

        return res
