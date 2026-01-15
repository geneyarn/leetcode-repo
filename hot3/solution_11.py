from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        maxLeft = 0
        maxRight = 0

        ans = 0
        i, j = 0, m - 1
        while i < j:
            maxLeft = max(height[i], maxLeft)
            maxRight = max(height[j], maxRight)

            ans = max(ans, min(maxLeft, maxRight) * (j - i))
            if maxLeft < maxRight:
                i += 1
            else:
                j -= 1

        return ans


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
