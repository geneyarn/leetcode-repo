from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        lMax = [0] * m
        lMax[0] = height[0]
        rMax = [0] * m
        rMax[-1] = height[-1]

        for i in range(1, m):
            lMax[i] = max(lMax[i - 1], height[i])

        for j in range(m - 2, -1, -1):
            rMax[j] = max(rMax[j + 1], height[j])

        res = 0
        for i in range(m):
            res += min(lMax[i], rMax[i]) - height[i]

        return res


result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)
