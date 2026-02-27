from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)

        s = 0

        for i in range(m - 1):
            s = max(s, i + nums[i])
            if s <= i:
                return False
        return s >= len(nums) - 1
