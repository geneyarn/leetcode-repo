from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s = 0

        for i in range(len(nums) - 1):
            s = max(s, i + nums[i])
            if s <= i:
                return False

        return s >= len(nums) - 1

# result = Solution().canJump([3,2,1,0,4])
result = Solution().canJump([0])
print(result)