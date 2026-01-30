from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxValue = 0
        for i in range(len(nums) - 1):
            maxValue = max(maxValue, i + nums[i])
            if maxValue <= i:
                return False
        return maxValue >= (len(nums) - 1)


# result = Solution().canJump([2, 3, 1, 1, 4])
# result = Solution().canJump([3, 2, 1, 0, 4])
result = Solution().canJump([2, 0, 0])
print(result)
