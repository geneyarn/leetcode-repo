from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        m = len(nums)

        preSum = [0] * (m + 1)
        for i in range(1, m + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        if preSum[m] - nums[0] == 0:
            return 0

        for i in range(1, m):
            if preSum[i] == preSum[m] - preSum[i + 1]:
                return i

        return -1


# result = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
# result = Solution().pivotIndex([1, 2, 3])
result = Solution().pivotIndex([2, 1, -1])
print(result)
