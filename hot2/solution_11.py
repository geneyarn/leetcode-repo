from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        lMax, rMax = height[0], height[m - 1]

        res = 0
        i, j = 0, m - 1
        while i <= j:
            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])

            res = max(res, min(rMax, lMax) * (j - i))
            if lMax < rMax:
                i += 1
            else:
                j -= 1
        return res


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
