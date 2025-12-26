from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        mx = 0

        for i in range(m - 1):
            mx = max(mx, i + nums[i])
            if mx <= i:
                return False

        return mx >= m - 1
