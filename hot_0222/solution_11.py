from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        i, j = 0, m - 1

        result = 0
        left = height[0]
        right = height[-1]
        while i < j:
            left = max(left, height[i])
            right = max(right, height[j])

            result = max(result, min(right, left) * (j - i))

            if left < right:
                i += 1
            else:
                j -= 1

        return result


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
