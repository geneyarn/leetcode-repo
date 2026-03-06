from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)

        jump = 0
        for i in range(m):
            if i <= jump:
                jump = max(jump, i + nums[i])
                if jump >= m - 1:
                    return True

        return False


result = Solution().canJump([2, 3, 1, 1, 4])
print(result)
