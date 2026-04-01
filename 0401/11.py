from cmath import inf
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        left = height[0]
        right = height[-1]

        ans = -inf
        i, j = 0, len(height) - 1
        while i < j:
            left = max(left, height[i])
            right = max(right, height[j])
            ans = max(min(left, right) * (j - i), ans)
            if left < right:
                i += 1
            else:
                j -= 1
        return ans


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
