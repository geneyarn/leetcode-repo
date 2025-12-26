from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preSum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            preSum[i] = preSum[i - 1] + (nums[i - 1] if nums[i - 1] > 0 else -1)

        val2Idx = {}
        res = 0
        for i in range(len(nums) + 1):
            if preSum[i] not in val2Idx:
                val2Idx[preSum[i]] = i
            else:
                res = max(res, i - val2Idx[preSum[i]])

        return res


result = Solution().findMaxLength([0, 1])
print(result)
