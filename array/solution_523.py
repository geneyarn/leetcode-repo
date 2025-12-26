from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = len(nums)
        preSum = [0] * (m + 1)

        for i in range(1, m + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        val2IndxMp = {}
        for i in range(m + 1):
            val = preSum[i] % k
            if val not in val2IndxMp:
                val2IndxMp[val] = i

        for i in range(1, m + 1):
            val = preSum[i] % k
            if val in val2IndxMp:
                if i - val2IndxMp[val] >= 2:
                    return True
        return False


# result = Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
# result = Solution().checkSubarraySum([23, 2, 6, 4, 7], 6)
# result = Solution().checkSubarraySum([23, 2, 6, 4, 7], 13)
result = Solution().checkSubarraySum([23, 2, 4, 6, 6], 7)
print(result)
