from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)

        ans = 0
        left, right = 0, m - 1

        while left < right:
            ans = max(ans, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
