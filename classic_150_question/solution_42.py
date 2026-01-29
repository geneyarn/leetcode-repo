from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        left = [0] * m
        right = [0] * m
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, m):
            left[i] = max(left[i - 1], height[i])
        for j in range(m - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        ans = 0
        for i in range(1, m - 1):
            ans += (min(left[i], right[i]) - height[i])

        return ans


result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)
